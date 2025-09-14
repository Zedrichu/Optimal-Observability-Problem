from z3 import Context
from typing import Optional

from dynamic_solvers.builders.ssp.SSPSpec import SSPSpec
from dynamic_solvers.builders.worlds import Line


class LineTPMC(Line, SSPSpec):
    def __init__(self, budget: int, goal: int, length: int, threshold: str, ctx: Optional[Context] = None):
        Line.__init__(self, length)
        SSPSpec.__init__(self, budget, goal, ctx)
        self.threshold = threshold


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 6:
        size = int(sys.argv[1])
        goal = int(sys.argv[2])
        budget = int(sys.argv[3])
        threshold = sys.argv[4]
        det = int(sys.argv[5])

        tpMC = LineTPMC(budget, goal, size, threshold)

        tpMC.declare_variables()
        tpMC.collect_constraints(threshold, determinism=det == 1)
