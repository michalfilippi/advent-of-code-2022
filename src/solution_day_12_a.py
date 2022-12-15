from collections import deque
from dataclasses import dataclass
from string import ascii_lowercase
from typing import Generator, Union

from base_solution import BaseSolution, TaskInput
from common import Position


@dataclass
class Heightmap:
    heightmap: list[list[int]]

    def height(self, position: Position) -> int:
        return self.heightmap[position.y][position.x]

    def possible_steps(
        self,
        from_position: Position,
        reverse: bool,
    ) -> Generator[Position, None, None]:
        for dx, dy in [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]:
            new_position = Position(from_position.x + dx, from_position.y + dy)
            if self.is_valid(new_position) and (
                (
                    not reverse
                    and self.height(new_position) - self.height(from_position) <= 1
                )
                or (
                    reverse
                    and self.height(from_position) - self.height(new_position) <= 1
                )
            ):
                yield new_position

    def is_valid(self, position: Position) -> bool:
        return 0 <= position.x < len(self.heightmap[0]) and 0 <= position.y < len(
            self.heightmap
        )

    def find_positions(self, height: int) -> Generator[Position, None, None]:
        for y, row in enumerate(self.heightmap):
            for x, h in enumerate(row):
                if h == height:
                    yield Position(x, y)


class SolutionDay12A(BaseSolution):

    INPUTS = {
        "test": TaskInput(
            file_name="day_12_test.txt",
            result=31,
        ),
        "puzzle": TaskInput(
            file_name="day_12_puzzle.txt",
            result=472,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        heightmap, start_position, end_position = self._get_heightmap(data)
        return self._get_path(heightmap, start_position, {end_position})

    @staticmethod
    def _get_heightmap(
        data: Generator[str, None, None]
    ) -> tuple[Heightmap, Position, Position]:
        transition_map = {c: i for i, c in enumerate(ascii_lowercase)}
        start_position = None
        end_position = None
        heightmap: list[list[int]] = []
        for line in data:
            row: list[int] = []
            for c in line:
                if c == "S":
                    start_position = Position(len(row), len(heightmap))
                    row.append(0)
                elif c == "E":
                    end_position = Position(len(row), len(heightmap))
                    row.append(len(ascii_lowercase) - 1)
                else:
                    row.append(transition_map[c])
            heightmap.append(row)

        if start_position is not None and end_position is not None:
            return Heightmap(heightmap), start_position, end_position
        else:
            raise ValueError()

    def _get_path(
        self,
        heightmap: Heightmap,
        start_position: Position,
        end_positions: set[Position],
        reverse: bool = False,
    ) -> int:
        queue = deque([(0, start_position)])
        visited = set()
        while len(queue):
            steps, position = queue.popleft()
            if position not in visited:
                if position in end_positions:
                    return steps

                visited.add(position)
                for new_position in heightmap.possible_steps(position, reverse):
                    queue.append((steps + 1, new_position))
        return -1
