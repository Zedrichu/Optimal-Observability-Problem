from typing import Unpack

from dynamic_solvers.builders.ssp.SSPSpec import SSPSpec
from dynamic_solvers.builders.worlds import Grid
from dynamic_solvers.builders.types import OperationKWArgs


class GridTPMC(Grid, SSPSpec):
    def __init__(self, budget: int, goal: int, width: int, height: int,
                 determinism: bool = False, **kwargs: Unpack[OperationKWArgs]):
        """Create a Grid SSP instance.

        Args:
            budget: Budget constraint (number of sensors allowed).
            goal: Goal state index.
            width: Width of the grid.
            height: Height of the grid.
            determinism: Use deterministic strategies (default: False).
            **kwargs: Additional parameters (ctx, verbose, bellman_format).
                See OOPSpec.__init__ for details.
        """
        Grid.__init__(self, width, height)
        SSPSpec.__init__(self, budget, goal, determinism, **kwargs)


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 6:
        size_x = int(sys.argv[1])
        size_y = int(sys.argv[2])
        goal = int(sys.argv[3])
        budget = int(sys.argv[4])
        threshold = sys.argv[5]
        det = int(sys.argv[6])

        tpMC = GridTPMC(budget, goal, size_x, size_y, determinism=det == 1)

        tpMC.declare_variables()
        tpMC.collect_constraints(threshold)
