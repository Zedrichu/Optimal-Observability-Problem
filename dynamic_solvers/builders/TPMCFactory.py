from enum import Enum, auto

from z3 import Context

from dynamic_solvers.builders.OOPSpec import OOPSpec
from dynamic_solvers.builders.pop.GridTPMC import GridTPMC as GridTPMCPOP
from dynamic_solvers.builders.pop.LineTPMC import LineTPMC as LineTPMCPOP
from dynamic_solvers.builders.pop.MazeTPMC import MazeTPMC as MazeTPMCPOP
from dynamic_solvers.builders.ssp.GridTPMC import GridTPMC as GridTPMCSSP
from dynamic_solvers.builders.ssp.LineTPMC import LineTPMC as LineTPMCSSP
from dynamic_solvers.builders.ssp.MazeTPMC import MazeTPMC as MazeTPMCSSP


class OOPVariant(Enum):
    POP = auto(),
    SSP = auto()


class PuzzleType(Enum):
    LINE = auto(),
    GRID = auto(),
    MAZE = auto()


def variant_from_string(s: str) -> OOPVariant:
  """Convert string argument to OOPVariant enum"""
  mapping = {
      'ssp': OOPVariant.SSP,
      'pop': OOPVariant.POP
  }
  if s.lower() not in mapping:
      raise ValueError(f"Invalid variant: {s}. Choose from: {list(mapping.keys())}")
  return mapping[s.lower()]

def puzzle_from_string(s: str) -> PuzzleType:
  """Convert string argument to PuzzleType enum"""
  mapping = {
      'line': PuzzleType.LINE,
      'grid': PuzzleType.GRID,
      'maze': PuzzleType.MAZE
  }
  if s.lower() not in mapping:
      raise ValueError(f"Invalid puzzle type: {s}. Choose from: {list(mapping.keys())}")
  return mapping[s.lower()]


class TPMCFactory:
    @staticmethod
    def create(oop_variant: OOPVariant, puzzle_type: PuzzleType, **kwargs) -> OOPSpec:
        if oop_variant == OOPVariant.POP:
            return TPMCFactory._create_pop_solver(puzzle_type, **kwargs)
        elif oop_variant == OOPVariant.SSP:
            return TPMCFactory._create_ssp_solver(puzzle_type, **kwargs)

    @staticmethod
    def _create_pop_solver(puzzle_type: PuzzleType, **kwargs) -> OOPSpec:
        if puzzle_type == PuzzleType.LINE:
            return LineTPMCPOP(budget=kwargs['budget'],
                               goal=kwargs['goal'],
                               length=kwargs['length'],)
        elif puzzle_type == PuzzleType.GRID:
            return GridTPMCPOP(budget=kwargs['budget'],
                               goal=kwargs['goal'],
                               width=kwargs['width'],
                               height=kwargs['height'],)
        elif puzzle_type == PuzzleType.MAZE:
            return MazeTPMCPOP(budget=kwargs['budget'],
                               goal=kwargs['goal'],
                               width=kwargs['width'],
                               depth=kwargs['height'],)

    @staticmethod
    def _create_ssp_solver(puzzle_type: PuzzleType, **kwargs) -> OOPSpec:
        if puzzle_type == PuzzleType.LINE:
            return LineTPMCSSP(budget=kwargs['budget'],
                               goal=kwargs['goal'],
                               length=kwargs['length'],
                               threshold=kwargs['threshold'])
        elif puzzle_type == PuzzleType.GRID:
            return GridTPMCSSP(budget=kwargs['budget'],
                               goal=kwargs['goal'],
                               width=kwargs['width'],
                               height=kwargs['height'],
                               threshold=kwargs['threshold'])
        elif puzzle_type == PuzzleType.MAZE:
            return MazeTPMCSSP(budget=kwargs['budget'],
                               goal=kwargs['goal'],
                               width=kwargs['width'],
                               depth=kwargs['height'],
                               threshold=kwargs['threshold'])
