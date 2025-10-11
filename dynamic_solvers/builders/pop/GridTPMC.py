from typing import Unpack

from dynamic_solvers.builders.pop.POPSpec import POPSpec
from dynamic_solvers.builders.worlds import Grid
from dynamic_solvers.builders.types import OperationKWArgs


class GridTPMC(Grid, POPSpec):
    def __init__(self, budget: int, goal: int, width: int, height: int,
                 determinism: bool = False, **kwargs: Unpack[OperationKWArgs]):
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
