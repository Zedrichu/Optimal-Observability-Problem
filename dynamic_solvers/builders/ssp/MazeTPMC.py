from typing import Unpack

from dynamic_solvers.builders.ssp.SSPSpec import SSPSpec
from dynamic_solvers.builders.worlds import Maze
from dynamic_solvers.builders.types import OperationKWArgs


class MazeTPMC(Maze, SSPSpec):
    def __init__(self, budget: int, goal: int, width: int, depth: int,
                 determinism: bool = False, **kwargs: Unpack[OperationKWArgs]):
        """Create a Maze SSP instance.

        Args:
            budget: Budget constraint (number of sensors allowed).
            goal: Goal state index.
            width: Width of the maze.
            depth: Depth of the maze.
            determinism: Use deterministic strategies (default: False).
            **kwargs: Additional parameters (ctx, verbose, bellman_format).
                See OOPSpec.__init__ for details.
        """
        Maze.__init__(self, width, depth)
        SSPSpec.__init__(self, budget, goal, determinism, **kwargs)


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
