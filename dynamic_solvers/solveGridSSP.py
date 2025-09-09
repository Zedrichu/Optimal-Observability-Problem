import re
from typing import List

from z3 import (z3, Q, Or)

from dynamic_solvers.SSPSpec import SSPSpec


class GridTPMC(SSPSpec):
    def __init__(self, budget: int, goal: int, width: int, height: int, threshold: str):
        size = width * height
        super().__init__(budget, size, goal)

        self.width = width
        self.height = height
        self.actions = ['l', 'r', 'u', 'd']
        self.threshold = threshold

        self.reset()

    def build_fully_observable_constraints(self) -> List[z3.BoolRef]:
        """
        Build basic POMDP constraints - a POMDP instance cannot perform better than the fully observable variant.
        Compute Manhattan distances between each state and the goal state based on the grid topology.
        """
        print('#A POMDP instance cannot perform better than the fully observable variant\n')
        constraints = []

        # Grid-specific bounds calculation
        goal_column = self.goal % self.width
        for s in range(self.size):
            column = s % self.width
            bound_value = abs(goal_column - column) + (abs(self.goal - s) // self.width)
            constraints.append(self.ExpRew[s] >= bound_value)

        self.console.print(constraints)
        return constraints

    def navigate(self, state: int, action_idx: int) -> int:
        """Navigate in 2D grid based on action"""
        action = self.actions[action_idx]
        x = state % self.width
        y = state // self.width

        if action == 'l':  # left
            if x != 0:
                return state - 1
        elif action == 'r':  # right
            if x != self.width - 1:
                return state + 1
        elif action == 'u':  # up
            if y != 0:
                return state - self.width
        else:  # action == 'd' (down)
            if y != self.height - 1:
                return state + self.width
        return state

    # size_x = 4; size_y = 3; column = 11 % 4 = 3
    # 3 -> 3 % 4 == 3 -> (11 - 3) // 4 == 2
    # 5 -> 5 % 4 == 1 -> (3 - 1) + 6 // 4 = 2 + 1 = 3
    # size_x -> size_y |
    # 0 1 2 3          v  5 4 3 2
    # 4 5 6 7             4 3 2 1
    # 8 9 10 11           3 2 1 0


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
        # Agent dropped in the grid under uniform distribution
        # Check if the minimal expected cost is below some threshold
        print(f"\n# Agent dropped uniformly in the grid\n"
              f"# Objective: check if the minimal expected cost is below some threshold '{threshold}'")

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


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 6:
        size_x = int(sys.argv[1])
        size_y = int(sys.argv[2])
        goal = int(sys.argv[3])
        budget = int(sys.argv[4])
        threshold = sys.argv[5]
        det = int(sys.argv[6])

        tpMC = GridTPMC(budget, goal, size_x, size_y, threshold)

        tpMC.declare_variables()


        ExpRew = tpMC.expected_rewards
        X = tpMC.strategy_rates
        Y = tpMC.observation_fun

        pomdp_constraints = tpMC.extend_fully_observable_pomdp_constraints(ExpRew)
        cost_constraints = tpMC.build_cost_reward_equations(ExpRew, X, Y)
        threshold_constraint = tpMC.build_threshold_constraint(ExpRew, threshold)
        strategy_constraints = tpMC.extend_strategy_constraints(X, determinism=det == 1)
        observation_constraints = tpMC.build_observation_constraints(Y)
        budget_constraint = tpMC.build_budget_constraint(Y, budget)

        solver = tpMC.solver
        solver.add(pomdp_constraints)
        solver.add(cost_constraints)
        solver.add(threshold_constraint)
        solver.add(strategy_constraints)
        solver.add(observation_constraints)
        solver.add(budget_constraint)

        tpMC.set_solver_options("results.txt", "reward.txt", 90000)

        try:
            result = tpMC.solve_benchmark()
            print(f" 🚀 Solve time: {result.solve_time:.4f}s")
        finally:
            tpMC.cleanup()