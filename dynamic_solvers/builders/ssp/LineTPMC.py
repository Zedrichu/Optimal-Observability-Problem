from typing import Unpack

from dynamic_solvers.builders.ssp.SSPSpec import SSPSpec
from dynamic_solvers.builders.worlds import Line
from dynamic_solvers.builders.types import OperationKWArgs


class LineTPMC(Line, SSPSpec):
    def __init__(self, budget: int, goal: int, length: int,
                 determinism: bool = False, **kwargs: Unpack[OperationKWArgs]):
        """Create a Line SSP instance.

        Args:
            budget: Budget constraint (number of sensors allowed).
            goal: Goal state index.
            length: Length of the line world.
            determinism: Use deterministic strategies (default: False).
            **kwargs: Additional parameters (ctx, verbose, bellman_format).
                See OOPSpec.__init__ for details.
        """
        Line.__init__(self, length)
        SSPSpec.__init__(self, budget, goal, determinism, **kwargs)


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 6:
        size = int(sys.argv[1])
        goal = int(sys.argv[2])
        budget = int(sys.argv[3])
        threshold = sys.argv[4]
        det = int(sys.argv[5])

        tpMC = LineTPMC(budget, goal, size, determinism=det == 1)

        tpMC.declare_variables()
        tpMC.collect_constraints(threshold)
