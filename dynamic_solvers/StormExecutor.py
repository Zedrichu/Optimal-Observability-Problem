import re
import subprocess
from dataclasses import dataclass
from typing import Optional

import stormpy
import stormpy.pomdp
from stormpy import BuilderOptions, PrismProgram
from stormpy.pomdp import BeliefExplorationModelCheckerOptionsDouble

from builders.POMDPSpec import POMDPAdapter
from builders.enums import PuzzleType
from builders.ssp import LineTPMC


@dataclass
class StormWorldConfig:
    """Configuration for a specific world type's pre-built model."""
    puzzle_type: PuzzleType
    model_path: str
    max_budget: int
    max_dim1: int                   # Line: length, Grid: width, Maze: width
    max_dim2: Optional[int] = None  # Grid: height, Maze: depth, Line: None

    def get_dimensions_dict(self) -> dict:
        """Get dimensions as a dictionary for easier access."""
        dims = {"dim1": self.max_dim1}
        if self.max_dim2 is not None:
            dims["dim2"] = self.max_dim2
        return dims

    def __str__(self) -> str:
        if self.max_dim2 is not None:
            return f"{self.puzzle_type.name}: {self.model_path} (max: {self.max_dim1}x{self.max_dim2})"
        return f"{self.puzzle_type.name}: {self.model_path} (max: {self.max_dim1})"


class StormModelRegistry:
    """Registry of available pre-built Storm models."""

    def __init__(self):
        self.configs: dict[PuzzleType, StormWorldConfig] = {}
        self._initialize_default_configs()

    def _initialize_default_configs(self):
        """Initialize with default model configurations."""
        self.register(StormWorldConfig(
            puzzle_type=PuzzleType.LINE,
            model_path="storm-integration/line.prism",
            max_budget=50,
            max_dim1=250,  # Update based on your actual model
        ))

        self.register(StormWorldConfig(
            puzzle_type=PuzzleType.GRID,
            model_path="storm-integration/grid.prism",
            max_budget=10,
            max_dim1=10,  # width - Update based on your actual model
            max_dim2=10,   # height
        ))

        self.register(StormWorldConfig(
            puzzle_type=PuzzleType.MAZE,
            model_path="storm-integration/maze.prism",
            max_budget=30,
            max_dim1=20,  # width - Update based on your actual model
            max_dim2=10,  # depth
        ))

    def register(self, config: StormWorldConfig):
        """Register a new model configuration."""
        self.configs[config.puzzle_type] = config

    def get(self, puzzle_type: PuzzleType) -> StormWorldConfig:
        """Get configuration for a puzzle type."""
        if puzzle_type not in self.configs:
            raise ValueError(f"No model configuration found for {puzzle_type}")
        return self.configs[puzzle_type]

    def __str__(self) -> str:
        lines = ["Available Storm Models:"]
        for config in self.configs.values():
            lines.append(f"  - {config}")
        return "\n".join(lines)


def _build_world_definition_const(pomdp: POMDPAdapter) -> dict[str, int]:
    world_consts = {
        "BUDGET": pomdp.budget,
        "GOAL": pomdp.goal,
    }
    dim1, dim2 = pomdp.get_dimensions()
    match pomdp.puzzle_type:
        case PuzzleType.LINE:
            world_consts.update({"LENGTH": dim1})
        case PuzzleType.GRID:
            world_consts.update({"WIDTH": dim1})
            world_consts.update({"HEIGHT": dim2})
        case PuzzleType.MAZE:
            world_consts.update({"WIDTH": dim1})
            world_consts.update({"HEIGHT": dim2})
    return world_consts
