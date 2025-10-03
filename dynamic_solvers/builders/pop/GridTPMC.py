from z3 import Context
from typing import Optional

from dynamic_solvers.builders.pop.POPSpec import POPSpec
from dynamic_solvers.builders.worlds import Grid


class GridTPMC(Grid, POPSpec):
    def __init__(self, budget: int, goal: int, width: int, height: int, determinism: bool = False, ctx: Optional[Context] = None, verbose: bool = False):
        Grid.__init__(self, width, height)
        POPSpec.__init__(self, budget, goal, determinism, ctx, verbose)


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 6:
        size = int(sys.argv[1])
        goal = int(sys.argv[2])
        budget = int(sys.argv[3])
        threshold = sys.argv[4]
        det = int(sys.argv[5])

        tpMC = GridTPMC(budget, goal, size, size, determinism=det == 1)

        tpMC.declare_variables()
        tpMC.collect_constraints(threshold)
