from z3 import Context
from typing import Optional

from dynamic_solvers.builders.pop.POPSpec import POPSpec
from dynamic_solvers.builders.worlds import Grid


class GridTPMC(Grid, POPSpec):
    def __init__(self, budget: int, goal: int, width: int, height: int, determinism: bool = False, **kwargs):
        """Create a Grid POP instance.

        Args:
            budget: Budget constraint (number of observation classes allowed).
            goal: Goal state index.
            width: Width of the grid.
            height: Height of the grid.
            determinism: Use deterministic strategies (default: False).
            **kwargs: Additional parameters (ctx, verbose, bellman_format).
                See OOPSpec.__init__ for details.
        """
        Grid.__init__(self, width, height)
        POPSpec.__init__(self, budget, goal, determinism, **kwargs)


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
