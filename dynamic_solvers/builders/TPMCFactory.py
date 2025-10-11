from enum import Enum, auto
from typing import Unpack

from dynamic_solvers.builders.types import DimensionKWArgs, OperationKWArgs, TPMCParams
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
    """Factory for creating dynamic TPMC problem instances with context builders.
    The creational method accepts keyword arguments declared by `TPMCParams`."""

    @staticmethod
    def create(oop_variant: OOPVariant, puzzle_type: PuzzleType, **kwargs: Unpack[TPMCParams]) -> OOPSpec:
        """
        Factory method that handles parameter selection and object creation based on variant and world.
        Client only needs to pass all available parameters; factory filters what's needed.

        Uses **kwargs pattern for flexible parameter passing without explicit listing.
        Type-safety is ensured by modern typed-dictionary unpacking.

        Args:
            oop_variant (OOPVariant) : Enum tag for the selected OOP variant
            puzzle_type (PuzzleType) : Enum tag for the selected puzzle type
            **kwargs (Unpacked[TPMCParams]) : Additional parameters declared by TypedDict `TPMCParams`

        Keyword Args:
            Core Problem Settings:
                budget (int): Budget constraint (number of observation classes allowed).
                goal (int): Goal state index.
                determinism (bool): Restrict to deterministic strategies (default: False).

            World-specific Dimension Parameters:
                length (int): Length of the world (Line).
                width (int): Width of the world (Grid/Maze).
                height (int): Height of the world (Grid) or Depth of the world (Maze).
                depth (int): Depth of the world (Maze) [internally mapped from `height`].

            Operational Parameters:
                ctx (Optional[Context]): Z3 context to use (default: None, creates fresh context).
                verbose (bool): Enable verbose output (default: False).
                bellman_format (Optional[Literal["default", "common", "adapted"]]): Format for Bellman equations

        Returns:
            OOPSpec : configured instance specification for OOP
        """
        op_params = TPMCFactory._extract_operation_params(**kwargs)
        dim_params = TPMCFactory._extract_dimension_params(puzzle_type, kwargs)

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
        return constructors[oop_variant][puzzle_type](
            # Explicit parameter passing for core settings
            budget=kwargs["budget"],
            goal=kwargs["goal"],
            determinism=kwargs.get("determinism", False),
            **dim_params,
            **op_params,
        )

    @staticmethod
    def _extract_operation_params(**kwargs: TPMCParams) -> OperationKWArgs:
        """Extract operational parameters common to all constructors."""
        res: OperationKWArgs = {}
        op_params = set(OperationKWArgs.__annotations__.keys())
        res.update({key: kwargs[key] for key in op_params if key in kwargs})
        return res

    @staticmethod
    def _extract_dimension_params(puzzle_type: PuzzleType, kwargs: TPMCParams) -> DimensionKWArgs:
        """Extract dimension-specific parameters based on world type."""
        if puzzle_type == PuzzleType.LINE:
            return {'length': kwargs['length']}
        elif puzzle_type == PuzzleType.GRID:
            return {'width': kwargs['width'], 'height': kwargs['height']}
        elif puzzle_type == PuzzleType.MAZE:
            # Maze uses 'depth' internally instead of 'height'
            return {'width': kwargs['width'], 'depth': kwargs['height']}
