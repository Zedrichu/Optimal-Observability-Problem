from z3 import Context

from dynamic_solvers.builders.pop.POPSpec import POPSpec
from dynamic_solvers.builders.worlds import Maze


class MazeTPMC(Maze, POPSpec):
    def __init__(self, ctx: Context,  budget: int, goal: int, width: int, depth: int):
        Maze.__init__(self, width, depth)
        POPSpec.__init__(self, ctx, budget, goal)


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 6:
        width = int(sys.argv[1])
        depth = int(sys.argv[2])
        goal = int(sys.argv[3])
        budget = int(sys.argv[4])
        threshold = sys.argv[5]
        det = int(sys.argv[6])

        tpMC = MazeTPMC(Context(), budget, goal, width, depth)

        tpMC.declare_variables()
        tpMC.collect_constraints(threshold, determinism=det == 1)
