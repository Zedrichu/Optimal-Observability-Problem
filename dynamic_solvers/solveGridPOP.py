from typing import List
from z3 import (z3)
from dynamic_solvers.POPSpec import POPSpec


class GridTPMC(POPSpec):
    def __init__(self, budget: int, goal: int, width: int, height: int):
        size = width * height
        super().__init__(budget, size, goal)

        self.width = width
        self.height = height
        self.actions = ['l', 'r', 'u', 'd']

        self.reset()

    def build_fully_observable_constraints(self) -> List[z3.BoolRef]:
        """
        Build basic POMDP constraints - a POMDP instance cannot perform better than the fully observable variant.
        Compute Manhattan distances between each state and the goal state based on the grid topology.
        """
        print('\n# A POMDP instance cannot perform better than the fully observable variant')
        constraints = []

        # Grid-specific bounds calculation
        goal_column = self.goal % self.width
        for s in range(self.size):
            column = s % self.width
            bound_value = abs(goal_column - column) + (abs(self.goal - s) // self.width)
            constraints.append(self.ExpRew[s] >= bound_value)

        self.console.print(constraints)
        return constraints

    def navigate(self, state: int, action_index: int) -> int:
        action = self.actions[action_index]
        x = state % self.width
        y = state // self.width

        if action == 'l':
            if x != 0:
                return state - 1
        elif action == 'r':
            if x != self.width - 1:
                return state + 1
        elif action == 'u':
            if y != 0:
                return state - self.width
        else:  # action == 'd' (down)
            if y != self.height - 1:
                return state + self.width
        return state


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 6:
        size = int(sys.argv[1])
        goal = int(sys.argv[2])
        budget = int(sys.argv[3])
        threshold = sys.argv[4]
        det = int(sys.argv[5])

        tpMC = GridTPMC(budget, goal, size, size)

        tpMC.declare_variables()
        tpMC.collect_constraints(threshold, determinism=det == 1)
        tpMC.set_solver_options("results.txt", "reward.txt", 90000)

        try:
            result = tpMC.solve_benchmark()
            print(f" 🚀  Solve time: {result.solve_time:.4f}s")
            # print(f"Setup time: {result.setup_time:.4f}s")
            # print(f"Memory used: {result.memory_used / 1024 / 1024:.2f} MB")
            # print(f"Constraints: {result.constraint_count}")
        finally:
            tpMC.cleanup()