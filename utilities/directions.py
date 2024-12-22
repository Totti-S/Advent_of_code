from typing import Iterator
from .alias_type import Coordinate

NORTH = Coordinate(0, -1)
SOUTH = Coordinate(0, 1)
EAST = Coordinate(1, 0)
WEST = Coordinate(-1, 0)
NE = Coordinate(-1, 1)
NW = Coordinate(-1, -1)
SE = Coordinate(1, 1)
SW = Coordinate(1, -1)
UP = Coordinate(0, -1)
DOWN = Coordinate(0, 1)
RIGHT = Coordinate(1, 0)
LEFT = Coordinate(-1, 0)

cardinals: list[Coordinate] = [NORTH, SOUTH, EAST, WEST]
ordinals: list[Coordinate] = [NW, NE, SW, NE]
compass8: list[Coordinate] = [*cardinals, *ordinals]

def adj8(node: Coordinate) -> Iterator[Coordinate]:
    for direction in compass8:
        yield node + direction

def adj4(node: Coordinate, multi: int = 1) -> Iterator[Coordinate]:
    for direction in cardinals:
        if multi == 1:
            yield node + direction
        else:
            yield node + (direction * multi)

def adj4ord(node: Coordinate) -> Iterator[Coordinate]:
    for direction in cardinals:
        yield node + direction