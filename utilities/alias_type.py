import typing as t
from dataclasses import dataclass

Mode = t.Literal["silver", "gold", "both"]

@dataclass(slots=True)
class Coordinate:
    x: int = 0
    y: int = 0
    N: t.ClassVar[tuple[int, int]] = (0,  1)
    S: t.ClassVar[tuple[int, int]] = (0, -1)
    E: t.ClassVar[tuple[int, int]] = (1, 0)
    W: t.ClassVar[tuple[int, int]] = (-1, 0)
    NE: t.ClassVar[tuple[int, int]] = (1, 1)
    NW: t.ClassVar[tuple[int, int]] = (-1, 1)
    SE: t.ClassVar[tuple[int, int]] = (1, -1)
    SW: t.ClassVar[tuple[int, int]] = (-1, -1)
    UP: t.ClassVar[tuple[int, int]] = N
    DOWN: t.ClassVar[tuple[int, int]] = S
    RIGHT: t.ClassVar[tuple[int, int]] = E
    LEFT: t.ClassVar[tuple[int, int]] = W

    def __sub__(self, other):
        if isinstance(other, (tuple, Coordinate)):
            x = self.x - other[0]
            y = self.y - other[1]
        elif isinstance(other, int):
            x = self.x - other
            y = self.y - other
        return Coordinate(x=x, y=y)

    def __isub__(self, other):
        return self.__sub__(other)

    def __add__(self, other):
        if isinstance(other, (tuple, Coordinate)):
            x = self.x + other[0]
            y = self.y + other[1]
        elif isinstance(other, int):
            x = self.x + other
            y = self.y + other
        return Coordinate(x=x, y=y)

    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, (tuple, Coordinate)):
            x = self.x * other[0]
            y = self.y * other[1]
        elif isinstance(other, int):
            x = self.x * other
            y = self.y * other
        return Coordinate(x=x, y=y)

    def __imul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other) -> bool:
        if isinstance(other, (tuple, Coordinate)):
            if isinstance(other, tuple) and len(other) > 2:
                return False
            return self.x == other[0] and self.y == other[1]
        return False

    def __iter__(self):
        yield self.x
        yield self.y

    def __getitem__(self, other: t.Literal[0, 1]):
        return self.x if not other else self.y

    def __setitem__(self, other: t.Literal[0, 1], item: int):
        if not other:
            self.x = item
        else:
            self.y = item

    @classmethod
    def is_cardinal_direction(cls, c) -> bool:
        assert isinstance(c, (tuple, Coordinate)),(
            f"'is_cardinal_direction' takes in only tuple or Coordinate. Input type: {type(c)}"
        )
        return bool(c[0] ^ c[1])

    @classmethod
    def get_cardinal_direction(cls, c):
        assert isinstance(c, (tuple, Coordinate)),(
            f"'get_cardinal_direction' takes in only tuple or Coordinate. Input type: {type(c)}"
        )
        if not Coordinate.is_cardinal_direction(c):
            return None
        norm_x = c[0] // abs(c[0]) if c[0] else 0
        norm_y = c[1] // abs(c[1]) if c[1] else 0
        return Coordinate(norm_x, norm_y)

class GRID:
    def __init__(
        self,
        x: int,
        y: int,
        starting_point: Coordinate | tuple = Coordinate(0,0),
        loopover: bool = False,
    ) -> None:
        self.x = x
        self.y = y
        assert 0 <= starting_point[0] < self.x, (
            f"Starting x is out of bounds max x: {self.x}, start x: {starting_point[0]}"
        )
        assert 0 <= starting_point[1] < self.y, (
            f"Starting x is out of bounds max y: {self.y}, start x: {starting_point[1]}"
        )
        if isinstance(starting_point, tuple):
            starting_point = Coordinate(*starting_point)
        self.current_point = starting_point
        self.loopover = loopover

    def move(self, dir: int | Coordinate | tuple[int, int]):
        self.current_point += dir
        for i, max_coord in enumerate([self.x, self.y]):
            if self.current_point[i] >= max_coord:
                if self.loopover:
                    self.current_point[i] %= (max_coord - 1)
                else:
                    self.current_point[i] = max_coord - 1
            elif self.current_point[i] < 0:
                if self.loopover:
                    self.current_point[i] %= -(max_coord - 1)
                    self.current_point[i] += max_coord
                else:
                    self.current_point[i] = 0

    def move_to_edge(self, dir: Coordinate | tuple[int, int]):
        cardinal_direction = Coordinate.get_cardinal_direction(dir)
        match (cardinal_direction):
            case Coordinate.N:
                self.current_point[1] = self.y - 1
            case Coordinate.S:
                self.current_point[1] = 0
            case Coordinate.E:
                self.current_point[0] = self.x - 1
            case Coordinate.W:
                self.current_point[0] = 0
            case None:
                pass


if __name__ == "__main__":
    grid = GRID(10, 10, (0, 0), loopover=True)

