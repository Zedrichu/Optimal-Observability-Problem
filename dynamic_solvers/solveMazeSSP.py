import re
from typing import List

from z3 import (z3, Q, Or)

from dynamic_solvers.SSPSpec import SSPSpec


class MazeTMPC(SSPSpec):
    def __init__(self, budget: int, goal: int, width: int, depth: int, threshold: str):
        size = width + 3 * (depth - 1)
        super().__init__(budget, size, goal)

        if width % 2 == 0:
            raise ValueError('Width must be odd for maze generation')

        self.width = width
        self.depth = depth
        self.actions = ['l', 'r', 'u', 'd']
        self.threshold = threshold

        self.reset()

    def build_fully_observable_constraints(self) -> List[z3.BoolRef]:
        """
        Build basic POMDP constraints - a POMDP instance cannot perform better than the fully observable variant.
        Compute shortest-path distances between each state and the goal state based on the maze topology.
        """
        print('\n#A POMDP instance cannot perform better than the fully observable variant')
        constraints = []

        goal_column = self.goal if self.goal < self.width \
                                else (self.goal - self.width) % 3 * (self.width // 2)
        goal_height = 0 if self.goal < self.width \
                        else (self.goal - self.width) // 3 + 1

        # Maze-specific bounds calculation
        for s in range(self.size):
            if s < self.width:
                bound_value = goal_height + abs(s - goal_column)
            else:
                column = (s - self.width) % 3 * (self.width // 2)
                row = (s - self.width) // 3 + 1
                diff = int(goal_column != column)
                bound_value = abs(column - goal_column) + abs(row - goal_height + 2 * goal_height * diff)
            constraints.append(self.ExpRew[s] >= bound_value)

        self.console.print(constraints)
        return constraints

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


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 7:
        width = int(sys.argv[1])
        depth = int(sys.argv[2])
        goal = int(sys.argv[3])
        budget = int(sys.argv[4])
        threshold = sys.argv[5]
        det = int(sys.argv[6])

        tpMC = MazeTMPC(budget, goal, width, depth, threshold)

        tpMC.declare_variables()

        solver = tpMC.solver

        ExpRew = tpMC.expected_rewards
        X = tpMC.strategy_rates
        Y = tpMC.observation_fun

        pomdp_constraints = tpMC.build_fully_observable_constraints(ExpRew)
        cost_constraints = tpMC.build_cost_reward_equations(ExpRew, X, Y)
        threshold_constraint = tpMC.build_threshold_constraint(ExpRew, threshold)
        strategy_constraints = tpMC.extend_strategy_constraints(X, determinism=det == 1)
        observation_constraints = tpMC.build_observation_constraints(Y)
        budget_constraint = tpMC.build_budget_constraint(Y, budget)

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