import typing as t
from enum import Enum

Mode = t.Literal["silver", "gold", "both"]

class Compass(Enum):
    North = (0, 1)
    South = (0, -1)
    East = (1, 0)
    West = (0, -1)