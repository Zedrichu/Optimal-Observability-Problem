import gc
import time
from abc import ABC, abstractmethod
from typing import List

from rich.console import Console
from z3 import Context, Solver, z3, Real, Q, Or, set_option, sat, unsat

from dynamic_solvers.BenchmarkResult import BenchmarkResult
from dynamic_solvers.utils import parse_threshold


class POPSpec(ABC):
    def __init__(self, budget: int, size: int, goal: int):
        self.budget = budget
        self.size = size
        self.goal = goal

        self.actions = []

        self.ExpRew = None  # Expected reward variables
        self.Y = None       # Observation function variables
        self.X = None       # Strategy mapping variables (action rates)

        self.exp_rew_evaluator = None

        self.ctx = None
        self.solver = None

        self.file_rewards = None
        self.file_results = None
        self.console = Console()

    @abstractmethod
    def build_fully_observable_constraints(self) -> List[z3.BoolRef]:
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
        observable_states = [s for s in range(self.size) if s != self.goal]

        self.ExpRew = self.declare_expected_rewards()
        self.Y = self.declare_observation_function(observable_states)
        self.X = self.declare_strategy_mapping()

    def declare_expected_rewards(self) -> List[z3.ArithRef]:
        # Expected cost/reward of reaching the goal from each corresponding state.
        print("\n# Expected cost/reward of reaching the goal from each corresponding state.")
        expected_rewards = [Real(f'pi{s}', self.ctx) for s in range(self.size)]
        print(expected_rewards)
        return expected_rewards

    def declare_observation_function(self, observable_states: List[int]) -> List[List[z3.ArithRef]]:
        # Choice of observations on the states (e.g. ys0o1 = 1 means that in state 0, observable 1 is observed)
        print("\n# Choice of observations (e.g. ys0o1 = 1 means that in state 0, observable 1 is observed)")
        state_to_observation = [[Real(f'ys{s}o{o+1}', self.ctx)
                                    for o in range(self.budget)]
                                    for s in observable_states]
        return state_to_observation

    def declare_strategy_mapping(self) -> List[List[z3.ArithRef]]:
        # Rates of randomized strategies
        print("\n# Rates of randomized strategies")
        observation_to_action = [[Real(f'xo{o+1}{act}', self.ctx)
                                    for act in self.actions]
                                    for o in range(self.budget)]
        return observation_to_action

    def build_cost_reward_equations(self) -> List[z3.BoolRef]:
        # Expected cost/reward equations from each world state
        print("# Expected cost/reward equations from each world state")

        equations = []
        for s in range(self.size):
            if s == self.goal:
                equations.append(self.ExpRew[s] == 0)
                continue

            # Build action terms for each direction using a transition function
            action_terms = []
            for a in range(len(self.actions)):
                # Decrement the state index after processing the goal state
                idx = s - 1 if s > self.goal else s

                obs_strategy_terms = [self.Y[idx][o] * self.X[o][a] for o in range(self.budget)]
                next_state = self.navigate(s, a)
                action_terms.append(sum(obs_strategy_terms) * (1 + self.ExpRew[next_state]))

            equations.append(self.ExpRew[s] == sum(action_terms))

        self.console.print(equations)
        return equations

    def build_threshold_constraint(self, threshold: str) -> bool:
        # Agent dropped in the world under uniform distribution
        # Check if the minimal expected cost is below some threshold
        print(f"\n# Agent dropped uniformly in the world"
              f"\n# Objective: check if the minimal expected cost is below some threshold `{threshold}`")

        sum_rewards = sum(self.ExpRew[s] for s in range(self.size) if s != self.goal)
        numerator, denominator, sign = parse_threshold(threshold)

        self.exp_rew_evaluator = sum_rewards * Q(1, self.size - 1, self.ctx)
        constraint = sign(sum_rewards * Q(1, self.size - 1, self.ctx), Q(numerator, denominator, self.ctx))

        self.console.print(constraint)
        return constraint

    def build_strategy_constraints(self, determinism: bool) -> List[z3.BoolRef]:
        # Randomised strategies (proper probability distributions)
        print('# Randomised strategies (proper probability distributions)')
        constraints = []
        act_no = len(self.actions)
        for o in range(self.budget):
            for act in range(act_no):
                constraints.append(self.X[o][act] >= 0)
                constraints.append(self.X[o][act] <= 1)
            sum_prob = sum(self.X[o][act] for act in range(act_no))
            constraints.append(sum_prob == 1)

        # TODO: Check for determinism first and apply binary constraints only (no need for range)
        if determinism:
            print('# Deterministic strategies activated (one-hot encoding or degenerate categorical distribution)\n')

            det_constraints = [Or(self.X[o][act] == 0, self.X[o][act] == 1, self.ctx)
                                    for act in range(act_no)
                                    for o in range(self.budget)]
            constraints.extend(det_constraints)

        self.console.print(constraints)
        return constraints

    def build_observation_constraints(self) -> List[z3.BoolRef]:
        # Observation function constraints - every state should be mapped to some observable class
        print("# Observation function constraints - every state should be mapped to some observable class")
        constraints = []
        for state_obs in self.Y:
            constraints.extend([Or(obs == 0, obs == 1, self.ctx) for obs in state_obs])

        print('# Every state should be mapped to exactly one equivalence class\n')
        constraints.extend([sum(state_obs) == 1 for state_obs in self.Y])

        self.console.print(constraints)
        return constraints

    def collect_constraints(self, threshold: str, determinism: bool):
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

    def set_solver_options(self, result_path: str, reward_path: str, timeout: int):
        set_option(max_args=1000000, max_lines=100000000)
        self.solver.set("timeout", timeout)
        self.file_results = open(result_path, "w")
        self.file_rewards = open(reward_path, "w")
        return

    def solve_benchmark(self) -> BenchmarkResult:

        # Solving phase timing
        solve_start = time.perf_counter()
        result = self.solver.check()
        solve_time = time.perf_counter() - solve_start

        # Get model if satisfiable
        model = self.solver.model() if result == sat else None

        if result == sat:
            model = self.solver.model()
            print(' ✅  Solution found!')
            self.file_results.write(str(model))
            self.file_rewards.write(str(model.eval(self.exp_rew_evaluator)))
        elif result == unsat:
            print(' ❌  No solution!')
            self.file_rewards.write('N/A')
        else:
            print(' ❔  Unknown!')

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
