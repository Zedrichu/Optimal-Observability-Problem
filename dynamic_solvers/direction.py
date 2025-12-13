from enum import Enum


class Direction(Enum):
    N  = ("N",  {"u"})
    S  = ("S",  {"d"})
    W  = ("W",  {"l"})
    E  = ("E",  {"r"})
    NE = ("NE", {"u", "r"})
    SE = ("SE", {"d", "r"})
    SW = ("SW", {"d", "l"})
    NW = ("NW", {"u", "l"})

    def __init__(self, symbol, actions):
        self.symbol = symbol
        self.actions = actions
