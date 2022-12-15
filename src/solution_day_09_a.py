from dataclasses import dataclass
from math import fabs
from typing import Generator, Union

from base_solution import BaseSolution, TaskInput
from common import Position


@dataclass(frozen=True)
class RopePosition(Position):
    def move(self, direction: str) -> "RopePosition":
        match direction:
            case "R":
                return RopePosition(self.x + 1, self.y)
            case "L":
                return RopePosition(self.x - 1, self.y)
            case "U":
                return RopePosition(self.x, self.y + 1)
            case "D":
                return RopePosition(self.x, self.y - 1)
            case _:
                raise ValueError(f"Unknown direction {direction}")

    def follow(self, other: "RopePosition") -> "RopePosition":
        dx = other.x - self.x
        dy = other.y - self.y
        if max(fabs(dx), fabs(dy)) > 1:
            x = self.x
            y = self.y

            if dx < 0:
                x -= 1
            elif dx > 0:
                x += 1
            if dy < 0:
                y -= 1
            elif dy > 0:
                y += 1
            return RopePosition(x, y)

        return self


class SolutionDay09A(BaseSolution):

    INPUTS = {
        "test": TaskInput(
            file_name="day_09_test.txt",
            result=13,
        ),
        "puzzle": TaskInput(
            file_name="day_09_puzzle.txt",
            result=5930,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        position_head = RopePosition(0, 0)
        position_tail = RopePosition(0, 0)
        visited = set()

        for line in data:
            direction, count_str = line.split()
            count = int(count_str)
            for _ in range(count):
                position_head = position_head.move(direction)
                position_tail = position_tail.follow(position_head)
                visited.add((position_tail.x, position_tail.y))

        return len(visited)
