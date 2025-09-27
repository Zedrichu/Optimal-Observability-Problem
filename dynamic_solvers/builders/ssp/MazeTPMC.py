from z3 import Context
from typing import Optional

from dynamic_solvers.builders.ssp.SSPSpec import SSPSpec
from dynamic_solvers.builders.worlds import Maze


class MazeTPMC(Maze, SSPSpec):
    def __init__(self, budget: int, goal: int, width: int, depth: int, determinism: bool = False, ctx: Optional[Context] = None, verbose: bool = False):
        Maze.__init__(self, width, depth)
        SSPSpec.__init__(self, budget, goal, determinism, ctx, verbose)


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 7:
        width = int(sys.argv[1])
        depth = int(sys.argv[2])
        goal = int(sys.argv[3])
        budget = int(sys.argv[4])
        threshold = sys.argv[5]
        det = int(sys.argv[6])

        tpMC = MazeTPMC(budget, goal, width, depth, determinism=det == 1)

        tpMC.declare_variables()
        tpMC.collect_constraints(threshold)
