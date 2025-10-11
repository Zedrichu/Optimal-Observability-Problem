from z3 import Context
from typing import Optional

from dynamic_solvers.builders.pop.POPSpec import POPSpec
from dynamic_solvers.builders.worlds import Line


class LineTPMC(Line, POPSpec):
    def __init__(self, budget: int, goal: int, length: int, determinism: bool = False, **kwargs):
        """Create a Line POP instance.

        Args:
            budget: Budget constraint (number of observation classes allowed).
            goal: Goal state index.
            length: Length of the line world.
            determinism: Use deterministic strategies (default: False).
            **kwargs: Additional parameters (ctx, verbose, bellman_format).
                See OOPSpec.__init__ for details.
        """
        Line.__init__(self, length)
        POPSpec.__init__(self, budget, goal, determinism, **kwargs)


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
