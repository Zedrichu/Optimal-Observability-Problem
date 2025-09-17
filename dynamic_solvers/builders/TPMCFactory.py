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
        """
        Factory method that handles parameter selection and object creation.
        Client only needs to pass all available parameters; factory filters what's needed.
        """
        if oop_variant == OOPVariant.POP:
            return TPMCFactory._create_pop_solver(puzzle_type, **kwargs)
        elif oop_variant == OOPVariant.SSP:
            return TPMCFactory._create_ssp_solver(puzzle_type, **kwargs)

    @staticmethod
    def _create_pop_solver(puzzle_type: PuzzleType, **kwargs) -> OOPSpec:
        # Factory extracts only the parameters each constructor needs
        common_params = TPMCFactory._extract_common_params(kwargs)

        if puzzle_type == PuzzleType.LINE:
            params = {**common_params, 'length': kwargs['length']}
            return LineTPMCPOP(**params)
        elif puzzle_type == PuzzleType.GRID:
            params = {**common_params, 'width': kwargs['width'], 'height': kwargs['height']}
            return GridTPMCPOP(**params)
        elif puzzle_type == PuzzleType.MAZE:
            params = {**common_params, 'width': kwargs['width'], 'depth': kwargs['height']}
            return MazeTPMCPOP(**params)

    @staticmethod
    def _create_ssp_solver(puzzle_type: PuzzleType, **kwargs) -> OOPSpec:
        # Factory extracts only the parameters each constructor needs
        common_params = TPMCFactory._extract_common_params(kwargs)
        ssp_params = {**common_params, 'threshold': kwargs['threshold']}

        if puzzle_type == PuzzleType.LINE:
            params = {**ssp_params, 'length': kwargs['length']}
            return LineTPMCSSP(**params)
        elif puzzle_type == PuzzleType.GRID:
            params = {**ssp_params, 'width': kwargs['width'], 'height': kwargs['height']}
            return GridTPMCSSP(**params)
        elif puzzle_type == PuzzleType.MAZE:
            params = {**ssp_params, 'width': kwargs['width'], 'depth': kwargs['height']}
            return MazeTPMCSSP(**params)

    @staticmethod
    def _extract_common_params(kwargs) -> dict:
        """Extract parameters common to all constructors."""
        common = {}
        for key in ['budget', 'goal', 'ctx', 'verbose']:
            if key in kwargs:
                common[key] = kwargs[key]
        return common
