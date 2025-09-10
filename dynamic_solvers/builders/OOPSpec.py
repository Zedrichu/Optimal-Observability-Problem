import gc
import time
from abc import ABC, abstractmethod
from typing import List

from rich.console import Console
from z3 import (Context, Solver,
                z3, set_option, sat, unsat,
                Real, Q, Or)

from dynamic_solvers.BenchmarkResult import BenchmarkResult
from dynamic_solvers.builders.worlds import World
from dynamic_solvers.utils import parse_threshold


class OOPSpec(World, ABC):
    def __init__(self, budget: int, goal: int):
        self.budget = budget
        self.goal = goal

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
    def declare_observation_function(self, observable_states: List[z3.ArithRef]) -> List[z3.ArithRef]:
        raise NotImplementedError()

    @abstractmethod
    def declare_strategy_mapping(self, *args) -> List[List[z3.ArithRef]]:
        raise NotImplementedError()

    def reset(self):
        """Reset for fresh solving context"""
        gc.collect()  # Clean memory before starting
        self.ctx = Context()
        self.solver = Solver(ctx=self.ctx)

    def declare_expected_rewards(self) -> List[z3.ArithRef]:
        # Expected cost/reward of reaching the goal from each corresponding state.
        print("\n# Expected cost/reward of reaching the goal from each corresponding state.")
        expected_rewards = [Real(f'pi{s}', self.ctx) for s in range(self.size)]
        self.console.print(expected_rewards)
        return expected_rewards

    def build_fully_observable_constraints(self) -> List[bool]:
        """
        Build basic POMDP constraints - a POMDP instance cannot perform better than the fully observable variant.
        """
        print('\n# A POMDP instance cannot perform better than the fully observable variant')
        constraints = [self.ExpRew[s] >= self.dist(s, self.goal) for s in range(self.size)]

        self.console.print(constraints)
        return constraints

    def build_bellman_equations(self) -> List[z3.BoolRef]:
        # Bellman equations for expected rewards in each world's state
        print("\n# Bellman equations for expected rewards in each world's state")

        equations = []
        for s in range(self.size):
            if s == self.goal:
                equations.append(self.ExpRew[s] == 0)
                continue

            # Build action terms for each direction using a transition function
            equation = 1
            for a in range(len(self.actions)):
                # Decrement the state index after processing the goal state
                idx = s - 1 if s > self.goal else s

                action_term = self.build_action_term(a, idx)
                next_state = self.navigate(s, a)
                equation += action_term * self.ExpRew[next_state]
            equations.append(self.ExpRew[s] == equation)

        self.console.print(equations)
        return equations

    @abstractmethod
    def build_action_term(self, action_idx: int, state_idx: int) -> z3.ArithRef:
        raise NotImplementedError()

    def build_threshold_constraint(self, threshold: str) -> bool:
        # Agent dropped in the world under uniform distribution
        # Check if the minimal expected cost is below some threshold
        print(f"\n# Agent dropped uniformly in the world"
              f"\n# Objective: check if the minimal expected cost is below some threshold `{threshold}`")

        # Generate the sum of expected reward variables for non-target states (uniform distribution)
        sumExpRew = sum(self.ExpRew[s] for s in range(self.size) if s != self.goal)
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

        # TODO: Check for determinism first and apply binary constraints only (no need for range)
        if determinism:
            print('# Deterministic strategies activated (one-hot encoding or degenerate categorical distribution)\n')
            for strategy in self.X:
                for rate in strategy:
                    constraints.append(Or(rate == 0, rate == 1, self.ctx))

        self.console.print(constraints)
        return constraints

    @abstractmethod
    def build_observation_constraints(self) -> List[z3.BoolRef]:
        raise NotImplementedError()

    @abstractmethod
    def collect_constraints(self, threshold: str, determinism: bool) -> List[z3.BoolRef]:
        raise NotImplementedError()

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
