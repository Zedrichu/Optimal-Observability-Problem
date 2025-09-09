from dynamic_solvers.POPSpec import POPSpec
from dynamic_solvers.builders.worlds import Maze


class MazeTPMC(Maze, POPSpec):
    def __init__(self, budget: int, goal: int, width: int, depth: int):
        Maze.__init__(self, width, depth)
        POPSpec.__init__(self, budget, goal)

        self.reset()


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 6:
        width = int(sys.argv[1])
        depth = int(sys.argv[2])
        goal = int(sys.argv[3])
        budget = int(sys.argv[4])
        threshold = sys.argv[5]
        det = int(sys.argv[6])

        tpMC = MazeTPMC(budget, goal, width, depth)

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
