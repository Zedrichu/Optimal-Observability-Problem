import gc
import time
from abc import ABC, abstractmethod
from typing import List

from rich.console import Console
from z3 import Context, Solver, z3, Real, sat, unsat, set_option, Or, Q

from dynamic_solvers.BenchmarkResult import BenchmarkResult
from dynamic_solvers.utils import parse_threshold


class SSPSpec(ABC):
    size: int
    actions: List[str]

    def __init__(self, budget: int, goal: int):
        self.budget = budget
        self.goal = goal

        self.ExpRew = None  # Expected reward variables
        self.Y = None  # Observation function variables
        self.X = None  # Strategy mapping variables (action rates)

        self.exp_rew_evaluator = None

        self.ctx = None
        self.solver = None

        self.file_rewards = None
        self.file_results = None
        self.console = Console()

    @abstractmethod
    def dist(self, state: int, target: int) -> int:
        raise NotImplementedError()

    @abstractmethod
    def navigate(self, state: int, action_index: int) -> int:
        raise NotImplementedError()

    def reset(self):
        """Reset for fresh solving context"""
        gc.collect()  # Clean memory before starting
        self.ctx = Context()
        self.solver = Solver(ctx=self.ctx)

    def declare_variables(self):
        # TODO! Use pre-computed dictionary for sensor mapping (especially with multiple goals)
        # O(1) lookup - minimal overhead, big readability gain
        # self.state_to_sensor = {state: idx for idx, state in enumerate(self.nongoal_states)}
        self.console.print("\n  ⚙️  Declaring variables...")

        nongoal_states = [s for s in range(self.size) if s != self.goal]
        self.ExpRew = self.declare_expected_rewards()
        self.Y = self.declare_observation_function(nongoal_states)
        self.X = self.declare_strategy_mapping(nongoal_states)

    def declare_expected_rewards(self) -> List[z3.ArithRef]:
        # Expected cost/reward of reaching the goal from each corresponding state.
        print("\n# Expected cost/reward of reaching the goal from each corresponding state.")
        expected_rewards = [Real(f'pi{s}', self.ctx) for s in range(self.size)]
        self.console.print(expected_rewards)
        return expected_rewards

    def declare_observation_function(self, sensor_states: List[int]) -> List[z3.ArithRef]:
        # Choice of observations on each non-goal state (state sensors)
        # e.g. `ys0 == 1` means that in state 0 the sensor is on, `ys0 == 0` - state sensor is off
        print("\n# Choice of observation on each non-goal state (state sensors that are on/off)")
        state_to_observation = [Real(f'ys{s}', self.ctx) for s in sensor_states]
        self.console.print(state_to_observation)
        return state_to_observation

    def declare_strategy_mapping(self, sensor_states: List[int]) -> List[List[z3.ArithRef]]:
        # Action rates of randomized strategies per state (when the sensor is on)
        print("\n# Action rates of randomized strategies per state (when sensor is on)")
        sensor_to_action = [[Real(f'xo{s}{act}', self.ctx) for act in self.actions] for s in sensor_states]
        # Default strategy variables per action (when no sensor is observed - unknown state)
        default_policy = [Real(f'x⊥{act}', self.ctx) for act in self.actions]
        sensor_to_action.append(default_policy)
        self.console.print(sensor_to_action)
        return sensor_to_action

    def build_fully_observable_constraints(self) -> List[bool]:
        """
        Build basic POMDP constraints - a POMDP instance cannot perform better than the fully observable variant.
        """
        print('\n# A POMDP instance cannot perform better than the fully observable variant')
        constraints = [self.ExpRew[s] >= self.dist(s, self.goal) for s in range(self.size)]

        self.console.print(constraints)
        return constraints

    def build_cost_reward_equations(self) -> List[z3.BoolRef]:
        # Expected cost/reward equations from each world state
        print("# Expected cost/reward equations from each world state")
        equations = []
        for s in range(self.size):
            if s == self.goal:
                equations.append(self.ExpRew[s] == 0)
                continue
            equation = 1
            for act in range(len(self.actions)):
                # Decrement the state index after processing the goal state
                idx = s - 1 if s > self.goal else s

                strategy = (1 - self.Y[idx]) * self.X[-1][act] + self.Y[idx] * self.X[idx][act]
                next_state = self.navigate(s, act)
                equation += strategy * self.ExpRew[next_state]
            equations.append(self.ExpRew[s] == equation)

        self.console.print(equations)
        return equations

    def build_threshold_constraint(self, threshold: str) -> bool:
        # Agent dropped in the world under uniform distribution
        # Check if the minimal expected cost is below some threshold
        print(f"\n# Agent dropped uniformly in the world"
              f"\n# Objective: check if the minimal expected cost is below some threshold '{threshold}'")

        # Generate the sum of expected reward variables for non-target states (uniform distribution)
        sumExpRew = sum([self.ExpRew[s] for s in range(self.size) if s != self.goal])
        numerator, denominator, sign = parse_threshold(threshold)

        self.exp_rew_evaluator = sumExpRew * Q(1, self.size - 1, self.ctx)
        constraint = sign(sumExpRew * Q(1, self.size - 1, self.ctx), Q(numerator, denominator, self.ctx))

        self.console.print(constraint)
        return constraint

    def build_strategy_constraints(self, determinism: bool) -> List[z3.BoolRef]:
        # Randomized strategies (proper probability distributions)
        print('\n# Randomized strategies (proper probability distributions)')
        constraints = []
        for strategy in self.X:
            for rate in strategy:
                constraints.append(rate >= 0)
                constraints.append(rate <= 1)
            constraints.append(sum(strategy) == 1)

        if determinism:
            print('\n# Deterministic strategies activated (one-hot encoding or degenerate categorical distribution)\n')
            for strategy in self.X:
                for rate in strategy:
                    constraints.append(Or(rate == 0, rate == 1))

        self.console.print(constraints)
        return constraints

    def build_observation_constraints(self) -> List[z3.BoolRef]:
        # Observation function constraints - every state should be mapped to some observable class
        # For SSP, 2 observation classes exist: activated sensor or unknown
        print(f"\n# Observation function constraints - every state should be mapped to some observable class"
              f"\n# For SSP, 2 observation classes exist: activated sensor or unknown")
        constraints = [Or(sensor == 0, sensor == 1) for sensor in self.Y]
        self.console.print(constraints)
        return constraints

    def build_budget_constraint(self) -> z3.BoolRef:
        # Budget constraint - total sensors used <= budget
        print("# Budget constraint - total no. of sensors activated <= budget")
        constraint = sum(self.Y) <= self.budget # ?? original mentions == budget
        self.console.print(constraint)
        return constraint

    def collect_constraints(self, threshold: str, determinism: bool):
        self.console.print("\n  🛠️  Building constraints...")

        bound_constraints = self.build_fully_observable_constraints()
        self.solver.add(bound_constraints)
        cost_constraints = self.build_cost_reward_equations()
        self.solver.add(cost_constraints)
        threshold_constraint = self.build_threshold_constraint(threshold)
        self.solver.add(threshold_constraint)
        strategy_constraints = self.build_strategy_constraints(determinism)
        self.solver.add(strategy_constraints)
        observation_constraints = self.build_observation_constraints()
        self.solver.add(observation_constraints)
        budget_constraint = self.build_budget_constraint()
        self.solver.add(budget_constraint)

    def set_solver_options(self, result_path: str, reward_path: str, timeout: int):
        set_option(max_args=1000000, max_lines=100000000)
        self.solver.set("timeout", timeout)
        self.file_results = open(result_path, "w")
        self.file_rewards = open(reward_path, "w")
        return

    def solve_benchmark(self) -> BenchmarkResult:

        # Solving phase timing for benchmarks
        solve_start = time.perf_counter()
        result = self.solver.check()
        solve_time = time.perf_counter() - solve_start

        # Get model if satisfiable
        model = self.solver.model() if result == sat else None

        print()
        if result == sat:
            model = self.solver.model()
            print(' ✅  Solution found!')
            self.file_results.write(str(model))
            self.file_rewards.write(str(model.eval(self.exp_rew_evaluator)))
        elif result == unsat:
            print(' ❌  No solution!')
            self.file_rewards.write('N/A')
        else:
            print(' ❔ Unknown!')

        return BenchmarkResult(
            solve_time=solve_time,
            result=result,
            model=model
        )

    def cleanup(self):
        if self.file_results:
            self.file_results.close()
        if self.file_rewards:
            self.file_rewards.close()

        # Clean up Z3 objects
        del self.solver
        del self.ctx
        gc.collect()
        pass
