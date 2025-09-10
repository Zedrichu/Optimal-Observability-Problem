from z3 import Context

from dynamic_solvers.builders.pop.POPSpec import POPSpec
from dynamic_solvers.builders.worlds import Grid


class GridTPMC(Grid, POPSpec):
    def __init__(self, ctx: Context, budget: int, goal: int, width: int, height: int):
        Grid.__init__(self, width, height)
        POPSpec.__init__(self, ctx, budget, goal)


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 6:
        size = int(sys.argv[1])
        goal = int(sys.argv[2])
        budget = int(sys.argv[3])
        threshold = sys.argv[4]
        det = int(sys.argv[5])

        tpMC = GridTPMC(Context(), budget, goal, size, size)

        tpMC.declare_variables()
        tpMC.collect_constraints(threshold, determinism=det == 1)
