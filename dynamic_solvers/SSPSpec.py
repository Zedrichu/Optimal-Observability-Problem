import gc
import time
from abc import ABC
from typing import List

from rich.console import Console
from z3 import Context, Solver, z3, Real, sat, unsat, set_option, Or

from dynamic_solvers.BenchmarkResult import BenchmarkResult


class SSPSpec(ABC):
    def __init__(self, budget: int, size: int, goal: int):
        self.budget = budget
        self.size = size
        self.goal = goal

        self.actions = []

        self.ExpRew = None  # Expected reward variables
        self.Y = None  # Observation function variables
        self.X = None  # Strategy mapping variables (action rates)

        self.exp_rew_evaluator = None

        self.ctx = None
        self.solver = None

        self.file_rewards = None
        self.file_results = None
        self.console = Console()

    def reset(self):
        """Reset for fresh solving context"""
        gc.collect()  # Clean memory before starting
        self.ctx = Context()
        self.solver = Solver(ctx=self.ctx)

    def declare_variables(self):
        # TODO! Use pre-compute dictionary for sensor mapping (especially with multiple goals)
        # O(1) lookup - minimal overhead, big readability gain
        # self.state_to_sensor = {state: idx for idx, state in enumerate(self.nongoal_states)}

        nongoal_states = [s for s in range(self.size) if s != self.goal]
        self.ExpRew = self.declare_expected_rewards()
        self.Y = self.declare_observation_function(nongoal_states)
        self.X = self.declare_strategy_mapping(nongoal_states)

    def declare_expected_rewards(self) -> List[z3.ArithRef]:
        # Expected cost/reward of reaching the goal from each corresponding state.
        print("# Expected cost/reward of reaching the goal from each corresponding state.")
        expected_rewards = [Real(f'pi{s}', self.ctx) for s in range(self.size)]
        self.console.print(expected_rewards)
        return expected_rewards

    def declare_observation_function(self, sensor_states: List[int]) -> List[z3.ArithRef]:
        # Choice of observations on each non-goal state (state sensors)
        # e.g. `ys0 == 1` means that in state 0 the sensor is on, `ys0 == 0` - state sensor is off
        print("# Choice of observation on each non-goal state (state sensors that are on/off)")
        state_to_observation = [Real(f'ys{s}', self.ctx) for s in sensor_states]
        self.console.print(state_to_observation)
        return state_to_observation

    def declare_strategy_mapping(self, sensor_states: List[int]) -> List[List[z3.ArithRef]]:
        # Action rates of randomized strategies per state (when the sensor is on)
        print("# Action rates of randomized strategies per state (when sensor is on)")
        sensor_to_action = [[Real(f'xo{s}{act}', self.ctx) for act in self.actions] for s in sensor_states]
        # Default strategy variables per action (when no sensor is observed - unknown state)
        default_policy = [Real(f'x⊥{act}', self.ctx) for act in self.actions]
        sensor_to_action.append(default_policy)
        self.console.print(sensor_to_action)
        return sensor_to_action

    def build_observation_constraints(self):
        # Observation function constraints - every state should be mapped to some observable class
        # For SSP, 2 observation classes exist: activated sensor or unknown
        print(f"\n# Observation function constraints - every state should be mapped to some observable class"
              f"\n# For SSP, 2 observation classes exist: activated sensor or unknown")
        constraints = [Or(sensor == 0, sensor == 1) for sensor in self.Y]
        self.console.print(constraints)
        return constraints

    def build_budget_constraint(self):
        # Budget constraint - total sensors used <= budget
        print("# Budget constraint - total no. of sensors activate <= budget")
        constraint = sum(self.Y) <= self.budget # ?? original mentions == budget
        self.console.print(constraint)
        return constraint

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

        if result == sat:
            model = self.solver.model()
            print(' ✅  Solution found!')
            self.file_results.write(str(model))
            self.file_rewards.write(str(model.eval(self.evaluator)))
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