from dataclasses import dataclass
from math import fabs


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def manhattan_distance(self, other: "Position") -> int:
        return round(fabs(self.x - other.x) + fabs(self.y - other.y))
