"""Type definitions for TPMC parameter passing.

This module contains TypedDict definitions used across the TPMC factory
and leaf constructors. Separated to avoid circular imports.
"""

from typing import TypedDict, Optional, Literal, Required, NotRequired
from z3 import Context


class DimensionKWArgs(TypedDict, total=False):
    """World dimension parameters as kwargs to World constructors.

    Attributes:
        length (int): Length of the world (Line).
        width (int): Width of the world (Grid/Maze).
        height (int): Height of the world (Grid, mapped to 'depth' for Maze internally).
        depth (int): Depth of the world (Maze, mapped from 'height' for Maze internally).
    """
    length: Optional[int]
    width: Optional[int]
    height: Optional[int]
    depth: Optional[int]


class OperationKWArgs(TypedDict, total=False):
    """Operational/solver parameters passed as kwargs to instance constructors.
    These parameters control solver behavior and output, not problem definition.

    Attributes:
        ctx (Optional[Context]): Z3 context to use (default: None, creates fresh context).
        verbose (bool): Enable verbose output (default: False).
        bellman_format (Optional[Literal["default", "common", "adapted"]]):
            Format for Bellman equations
    """
    ctx: Optional[Context]
    verbose: bool
    bellman_format: Optional[Literal["default", "common", "adapted"]]
    bool_encoding: Optional[bool]


class TPMCParams(DimensionKWArgs, OperationKWArgs):
    """Combined kwargs set for TPMC factory (dimensions + operations + core).

    Attributes:
        budget (int): Budget constraint (number of observation classes allowed).
        goal (int): Goal state index.
        determinism (bool): Restrict to deterministic strategies (default: False).
    """
    # Core (mandatory) problem settings
    budget: Required[int]
    goal: Required[int]
    determinism: NotRequired[bool] # Can be inferred as False if missing
