from dynamic_solvers.builders.ssp.SSPSpec import SSPSpec
from dynamic_solvers.builders.worlds import Grid


class GridTPMC(Grid, SSPSpec):
    def __init__(self, budget: int, goal: int, width: int, height: int, threshold: str):
        Grid.__init__(self, width, height)
        SSPSpec.__init__(self, budget, goal)
        self.threshold = threshold

        self.reset()


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
