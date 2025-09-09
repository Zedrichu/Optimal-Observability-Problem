from typing import List

from z3 import (z3)

from dynamic_solvers.SSPSpec import SSPSpec


class LineTPMC(SSPSpec):
    def __init__(self, budget: int, goal: int, length: int, threshold: str):
        super().__init__(budget, length, goal)
        self.threshold = threshold

        self.actions = ['l', 'r']

        self.reset()

    def build_fully_observable_constraints(self) -> List[z3.BoolRef]:
        """
        Build basic POMDP constraints - a POMDP instance cannot perform better than the fully observable variant.
        """
        print('\n#A POMDP instance cannot perform better than the fully observable variant')
        constraints = [self.ExpRew[s] >= abs(self.goal - s) for s in range(self.size)]

        self.console.print(constraints)
        return constraints

    def navigate(self, state: int, action_idx: int) -> int:
        action = self.actions[action_idx]
        if action == 'l':
            return max(state - 1, 0)
        else: # action == 'r'
            return min(state + 1, self.size - 1)


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 6:
        size = int(sys.argv[1])
        goal = int(sys.argv[2])
        budget = int(sys.argv[3])
        threshold = sys.argv[4]
        det = int(sys.argv[5])

        tpMC = LineTPMC(budget, goal, size, threshold)

        tpMC.declare_variables()
        tpMC.collect_constraints(threshold, determinism=det == 1)

        tpMC.set_solver_options("results.txt", "reward.txt", 90000)

        try:
            result = tpMC.solve_benchmark()
            print(f" 🚀 Solve time: {result.solve_time:.4f}s")
            # print(f"Setup time: {result.setup_time:.4f}s")
            # print(f"Memory used: {result.memory_used / 1024 / 1024:.2f} MB")
            # print(f"Constraints: {result.constraint_count}")
        finally:
            tpMC.cleanup()
