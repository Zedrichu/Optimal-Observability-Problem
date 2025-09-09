from dynamic_solvers.SSPSpec import SSPSpec
from dynamic_solvers.builders.worlds import Line


class LineTPMC(Line, SSPSpec):
    def __init__(self, budget: int, goal: int, length: int, threshold: str):
        Line.__init__(self, length)
        SSPSpec.__init__(self, budget, goal)
        self.threshold = threshold

        self.reset()


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
