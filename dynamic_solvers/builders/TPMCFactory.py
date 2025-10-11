from enum import Enum, auto
from typing import TypedDict, Optional, Unpack, Literal

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


class TPMCKWArgs(TypedDict, total=False):
    """Keyword arguments for TPMC constructors."""
    # Problem settings
    budget: int
    goal: int
    determinism: bool
    # Operations and verbosity/logging
    ctx: Optional[Context]
    verbose: bool
    # Reproducibility add-ons for experiments/optimizations
    bellman_format: Optional[Literal["default", "common", "adapted"]]
    # Dimension key-word arguments
    length: Optional[int]
    width: Optional[int]
    height: Optional[int]


class TPMCFactory:
    """Factory for creating dynamic TPMC problem instances with context builders.

    Common parameters
    -----------------
    All create methods accept keyword arguments declared by `TPMCKWArgs`:
        budget : int
            Budget constraint (number of sensors/observation classes allowed)
        goal : int
            Index of the goal state in the world
        determinism : bool, optional
            Use deterministic strategies (default: False)
        bellman_format : str, optional
            Bellman equation format: "default", "common", or "adapted" (default: "default")
        ctx : z3.Context, optional
            Z3 context for solver (default: creates new context)
        verbose : bool, optional
            Enable verbose output (default: False)

    Dimension Parameters
    --------------------
    World-specific parameters:
        length : int
            Required for Line worlds
        width : int
            Required for Grid/Maze worlds
        height : int
            Required for Grid/Maze worlds (mapped to 'depth' for Maze internally)
    """
    # Define parameter sets for TPMC constructors as class constants for maintainability
    COMMON_PARAMS = [
        'budget', 'goal',
        'determinism',
        'ctx', 'verbose',
        'bellman_format'
    ]

    @staticmethod
    def create(oop_variant: OOPVariant, puzzle_type: PuzzleType, **kwargs: Unpack[TPMCKWArgs]) -> OOPSpec:
        """
        Factory method that handles parameter selection and object creation based on variant and world.
        Client only needs to pass all available parameters; factory filters what's needed.

        Uses **kwargs pattern for flexible parameter passing without explicit listing.
        Type-safety is ensured by modern typed-dictionary unpacking.

        Args:
            oop_variant : OOPVariant
            puzzle_type : PuzzleType
            **kwargs : Unpacked[TPMCKWArgs]
                Additional parameters
        """
        common = TPMCFactory._extract_common_params(kwargs)
        dimension = TPMCFactory._extract_dimension_params(puzzle_type, kwargs)
        # Merge common and dimension-specific params
        params = {**common, **dimension}

        # Dispatch to appropriate constructor based on problem variant and then puzzle type
        constructors = {
            OOPVariant.POP: {
                PuzzleType.LINE: LineTPMCPOP,
                PuzzleType.GRID: GridTPMCPOP,
                PuzzleType.MAZE: MazeTPMCPOP
            },
            OOPVariant.SSP: {
                PuzzleType.LINE: LineTPMCSSP,
                PuzzleType.GRID: GridTPMCSSP,
                PuzzleType.MAZE: MazeTPMCSSP
            },
        }
        return constructors[oop_variant][puzzle_type](**params)

    @staticmethod
    def _extract_common_params(kwargs) -> dict:
        """Extract parameters common to all constructors."""
        return {key: kwargs[key] for key in TPMCFactory.COMMON_PARAMS if key in kwargs}

    @staticmethod
    def _extract_dimension_params(puzzle_type: PuzzleType, kwargs) -> dict:
        """Extract dimension-specific parameters based on world type."""
        if puzzle_type == PuzzleType.LINE:
            return {'length': kwargs['length']}
        elif puzzle_type == PuzzleType.GRID:
            return {'width': kwargs['width'], 'height': kwargs['height']}
        elif puzzle_type == PuzzleType.MAZE:
            # Maze uses 'depth' internally instead of 'height'
            return {'width': kwargs['width'], 'depth': kwargs['height']}
