from typing import List

from z3 import (z3)

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
        tpMC.collect_constraints(threshold, determinism=det == 1)

        tpMC.set_solver_options("results.txt", "reward.txt", 90000)

        try:
            result = tpMC.solve_benchmark()
            print(f" 🚀 Solve time: {result.solve_time:.4f}s")
        finally:
            tpMC.cleanup()
