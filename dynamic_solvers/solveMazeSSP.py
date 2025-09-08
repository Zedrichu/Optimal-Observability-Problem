import gc
import re
import time
from logging import Logger
from typing import List
from rich.console import Console
from z3 import (Context, Solver,
                z3, sat, unsat, set_option,
                Real, Q, Or)

from dynamic_solvers.BenchmarkResult import BenchmarkResult


class MazeSSPChain:
    """
    Z3 API solver for "Maze" instances in the SSP problem with benchmarking

    Part of the OOP problem suites.
    """

    def __init__(self, budget: int, goal: int, height: int, width: int, threshold: str):
        self.budget = budget
        self.goal = goal
        self.height = height
        self.width = width
        self.threshold = threshold

        if width % 2 == 0:
            raise ValueError('Width must be odd for maze generation')

        self.size = self.width + (self.height - 1) * 3

        self.actions = ['l', 'r', 'u', 'd']

        self.expected_rewards = None
        self.observation_fun = None
        self.strategy_rates = None

        self.ctx = None
        self.solver = None

        self.evaluator = None
        self.console = Console()
        self.logger = Logger("MazeSSPChain")

        self.file_results = None
        self.file_rewards = None

        self.reset()

    def reset(self):
        """Reset for fresh solving context"""
        gc.collect()  # Clean memory before starting
        self.ctx = Context()
        self.solver = Solver(ctx=self.ctx)

    def declare_variables(self):
        nongoal_states = [s for s in range(self.size) if s != self.goal]
        self.expected_rewards = self.compute_expected_rewards(self.size)
        self.observation_fun = self.create_observation_maps(nongoal_states)
        self.strategy_rates = self.create_policy_maps(nongoal_states)

    def compute_expected_rewards(self, size: int) -> List[z3.ArithRef]:
        # Expected cost/reward of reaching the goal from each corresponding state.
        print("# Expected cost/reward of reaching the goal from each corresponding state.")
        expected_rewards = [Real(f'pi{s}', self.ctx) for s in range(size)]
        self.console.print(expected_rewards)
        return expected_rewards

    def create_observation_maps(self, sensor_states: List[int]) -> List[z3.ArithRef]:
        # Choice of observations on each non-goal state (state sensors)
        # e.g. `ys0 == 1` means that in state 0 the sensor is on, `ys0 == 0` - state sensor is off
        print("# Choice of observation on each non-goal state (state sensors that are on/off)")
        state_to_observation = [Real(f'ys{s}', self.ctx) for s in sensor_states]
        self.console.print(state_to_observation)
        return state_to_observation

    def create_policy_maps(self, sensor_states: List[int]) -> List[List[z3.ArithRef]]:
        # Action rates of randomized strategies per state (when the sensor is on)
        print("# Action rates of randomized strategies per state (when sensor is on)")
        sensor_to_action = [[Real(f'xo{s}{act}', self.ctx) for act in self.actions] for s in sensor_states]
        # Default strategy variables per action (when no sensor is observed - unknown state)
        default_policy = [Real(f'x⊥{act}', self.ctx) for act in self.actions]
        sensor_to_action.append(default_policy)
        self.console.print(sensor_to_action)
        return sensor_to_action

    def extend_fully_observable_pomdp_constraints(self, exp_rewards: List[z3.ArithRef]) -> List[z3.BoolRef]:
        """
        Build basic POMDP constraints - a POMDP instance cannot perform better than the fully observable variant.
        Compute Manhattan distances between each state and the goal state based on the maze topology.
        """
        print('\n#A POMDP instance cannot perform better than the fully observable variant')

        # Maze-specific bounds calculation
        pomdp_bounds = []
        goal_column = self.goal if self.goal < self.width \
                                else (self.goal - self.width) % 3 * (self.width // 2)
        goal_height = 0 if self.goal < self.width else (self.goal - self.width) // 3 + 1
        for s in range(self.size):
            if s < self.width:
                bound_value = goal_height + abs(s - goal_column)
            else:
                column = (s - self.width) % 3 * (self.width // 2)
                row = (s - self.width) // 3 + 1
                diff = int(goal_column != column)
                bound_value = abs(column - goal_column) + abs(row - goal_height + 2 * goal_height * diff)
            pomdp_bounds.append(exp_rewards[s] >= bound_value)

    def navigate(self, state: int, action_idx: int) -> int:
        """Navigate in 2D maze based on action"""
        action = self.actions[action_idx]

        if action == 'l':
            if 0 < state < self.width:
                return state - 1
        elif action == 'r':
            if 0 <= state < self.width - 1:
                return state + 1
        elif action == 'u':
            if state == self.width:
                return 0
            elif state == self.width + 1:
                return (self.width - 1) // 2
            elif state >= self.width + 2:
                return state - 3
        else:  # action == 'd'
            if state == 0:
                return self.width
            elif state == (self.width - 1) // 2:
                return self.width + 1
            elif self.width <= state < self.size - 3:
                return state + 3
        return state

    def build_cost_reward_equations(self, ExpRew, X, Y):
        # Expected cost/reward equations from each world state
        print("# Expected cost/reward equations from each world state")
        cost_equations = []
        for s in range(self.size):
            if s == self.goal:
                cost_equations.append(ExpRew[s] == 0)
                continue
            equation = 1
            for act in range(len(self.actions)):
                # After the goal state, the index is decremented (offset from states)
                idx = s - 1 if s > self.goal else s
                strategy = (1 - Y[idx]) * X[-1][act] + Y[idx] * X[idx][act]
                next_state = self.navigate(s, act)
                equation += strategy * ExpRew[next_state]
            cost_equations.append(ExpRew[s] == equation)
        self.console.print(cost_equations)
        return cost_equations

    def build_threshold_constraint(self, ExpRew, threshold: str):
        # Agent dropped in the maze under uniform distribution
        # Check if the minimal expected cost is below some threshold
        print(f"\n# Agent dropped uniformly in the maze"
              f"\n# Objective: check if the minimal expected cost is below some threshold '{threshold}'")

        # Generate the sum of expected reward variables for non-target states (uniform distribution)
        sumExpRew = sum([ExpRew[s] for s in range(self.size) if s != self.goal])
        sign_idx = threshold.find('<')
        if sign_idx == -1:
            return ValueError("No sign in threshold")
        sign = (lambda x, y: x <= y) if threshold[sign_idx + 1] == '=' else (lambda x, y: x < y)
        numerator, denominator = map(int, re.findall(r"\d+", threshold))

        self.evaluator = sumExpRew * Q(1, self.size - 1, self.ctx)

        threshold_constraint = sign(sumExpRew * Q(1, self.size - 1, self.ctx), Q(numerator, denominator, self.ctx))
        self.console.print(threshold_constraint)
        return threshold_constraint

    def extend_strategy_constraints(self, X: List[List[z3.ArithRef]], determinism: bool):
        # Randomized strategies (proper probability distributions)
        print('\n# Randomized strategies (proper probability distributions)')
        constraints = []
        for strategy in X:
            for rate in strategy:
                constraints.append(rate >= 0)
                constraints.append(rate <= 1)
            sum_prob = sum(strategy)
            constraints.append(sum_prob == 1)

        if determinism:
            print('\n# Deterministic strategies activated (one-hot encoding or degenerate categorical distribution)\n')
            for strategy in X:
                for rate in strategy:
                    constraints.append(Or(rate == 0, rate == 1))

        self.console.print(constraints)
        return constraints

    def extend_observation_constraints(self, Y: List[z3.ArithRef]):
        # Observation function constraints - every state should be mapped to some observable class
        print("# Observation function constraints - every state should be mapped to some observable class")
        constraints = [Or(sensor == 0, sensor == 1) for sensor in Y]
        self.console.print(constraints)
        return constraints

    def build_budget_constraint(self, Y: List[z3.ArithRef], budget: int):
        # Budget constraint - total sensors used <= budget
        print("# Budget constraint - total no. of sensors activate <= budget")
        budget_constraint = sum(Y) <= budget # ?? original mentions == budget
        self.console.print(budget_constraint)
        return budget_constraint

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
            print(' ❌ No solution!')
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


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 7:
        height = int(sys.argv[1])
        width = int(sys.argv[2])
        goal = int(sys.argv[3])
        budget = int(sys.argv[4])
        threshold = sys.argv[5]
        det = int(sys.argv[6])

        tpMC = MazeSSPChain(budget, goal, height, width, threshold)

        tpMC.declare_variables()

        solver = tpMC.solver

        ExpRew = tpMC.expected_rewards
        X = tpMC.strategy_rates
        Y = tpMC.observation_fun

        pomdp_constraints = tpMC.extend_fully_observable_pomdp_constraints(ExpRew)
        cost_constraints = tpMC.build_cost_reward_equations(ExpRew, X, Y)
        threshold_constraint = tpMC.build_threshold_constraint(ExpRew, threshold)
        strategy_constraints = tpMC.extend_strategy_constraints(X, determinism=det == 1)
        observation_constraints = tpMC.extend_observation_constraints(Y)
        budget_constraint = tpMC.build_budget_constraint(Y, budget)

        solver.add(pomdp_constraints)
        solver.add(cost_constraints)
        solver.add(threshold_constraint)
        solver.add(strategy_constraints)
        solver.add(observation_constraints)
        solver.add(budget_constraint)

        tpMC.set_solver_options("results.txt", "reward.txt")

        try:
            result = tpMC.solve_benchmark()
            print(f" 🚀 Solve time: {result.solve_time:.4f}s")
        finally:
            tpMC.cleanup()