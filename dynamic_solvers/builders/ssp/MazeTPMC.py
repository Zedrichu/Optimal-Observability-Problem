from dynamic_solvers.builders.ssp.SSPSpec import SSPSpec
from dynamic_solvers.builders.worlds import Maze


class MazeTMPC(Maze, SSPSpec):
    def __init__(self, budget: int, goal: int, width: int, depth: int, threshold: str):
        Maze.__init__(self, width, depth)
        SSPSpec.__init__(self, budget, goal)
        self.threshold = threshold

        self.reset()


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
