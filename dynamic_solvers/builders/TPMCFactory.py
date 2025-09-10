from enum import Enum

from dynamic_solvers.builders.OOPSpec import OOPSpec
from dynamic_solvers.builders.pop.GridTPMC import GridTPMC as GridTPMCPOP
from dynamic_solvers.builders.pop.LineTPMC import LineTPMC as LineTPMCPOP
from dynamic_solvers.builders.pop.MazeTPMC import MazeTPMC as MazeTPMCPOP
from dynamic_solvers.builders.ssp.GridTPMC import GridTPMC as GridTPMCSSP
from dynamic_solvers.builders.ssp.LineTPMC import LineTPMC as LineTPMCSSP
from dynamic_solvers.builders.ssp.MazeTPMC import MazeTPMC as MazeTPMCSSP


class OOPVariant(Enum):
    POP = 1,
    SSP = 2


class PuzzleType(Enum):
    LINE = 1,
    GRID = 2,
    MAZE = 3


class TPMCFactory:
    @staticmethod
    def create(oop_variant: OOPVariant, puzzle_type: PuzzleType, **kwargs) -> OOPSpec:
        if oop_variant == OOPVariant.POP:
            if puzzle_type == PuzzleType.LINE:
                return LineTPMCPOP(**kwargs)
            elif puzzle_type == PuzzleType.GRID:
                return GridTPMCPOP(**kwargs)
            elif puzzle_type == PuzzleType.MAZE:
                return MazeTPMCPOP(**kwargs)
        elif oop_variant == OOPVariant.SSP:
            if puzzle_type == PuzzleType.LINE:
                return LineTPMCSSP(**kwargs)
            elif puzzle_type == PuzzleType.GRID:
                return GridTPMCSSP(**kwargs)
            elif puzzle_type == PuzzleType.MAZE:
                return MazeTPMCSSP(**kwargs)
        raise ValueError("Invalid OOPVariant or PuzzleType")
