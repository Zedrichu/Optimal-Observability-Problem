from typing import List

from z3 import (z3)

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
        tpMC.collect_constraints(threshold, determinism=det == 1)

        tpMC.set_solver_options("results.txt", "reward.txt", 90000)

        try:
            result = tpMC.solve_benchmark()
            print(f" 🚀 Solve time: {result.solve_time:.4f}s")
        finally:
            tpMC.cleanup()
