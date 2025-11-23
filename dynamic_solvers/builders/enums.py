from enum import Enum, auto


class OOPVariant(Enum):
    POP = auto(),
    SSP = auto()


class PuzzleType(Enum):
    LINE = auto(),
    GRID = auto(),
    MAZE = auto()
