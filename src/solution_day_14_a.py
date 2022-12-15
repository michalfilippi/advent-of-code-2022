from dataclasses import dataclass, field
from itertools import count
from typing import Generator, Optional, Union

from base_solution import BaseSolution, TaskInput
from common import Position


class SandOverFlow(Exception):
    pass


@dataclass(frozen=True)
class CavePosition(Position):
    def drop_positions(self) -> Generator["CavePosition", None, None]:
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            yield CavePosition(self.x + dx, self.y + dy)


@dataclass
class CaveSlice:
    rocks: set[CavePosition] = field(default_factory=set)
    sand: set[CavePosition] = field(default_factory=set)
    _bottom: Optional[int] = None
    hard_bottom_offset: Optional[int] = None

    def is_empty(self, position: CavePosition) -> bool:
        return (
            position not in self.rocks
            and position not in self.sand
            and (
                self.hard_bottom_offset is None
                or position.y < (self.bottom + self.hard_bottom_offset)
            )
        )

    @property
    def bottom(self) -> int:
        if self._bottom is None:
            self._bottom = max(rock_position.y for rock_position in self.rocks)
        return self._bottom

    def drop(self, from_position: CavePosition) -> CavePosition:
        if from_position.y > self.bottom and self.hard_bottom_offset is None:
            raise SandOverFlow()
        for position in from_position.drop_positions():
            if self.is_empty(position):
                return self.drop(position)
        return from_position


class SolutionDay14A(BaseSolution):

    INPUTS = {
        "test": TaskInput(
            file_name="day_14_test.txt",
            result=24,
        ),
        "puzzle": TaskInput(
            file_name="day_14_puzzle.txt",
            result=592,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        cave_slice = self._get_cave_slice(data)
        drop_position = CavePosition(500, 0)
        for c in count(0):
            try:
                p = cave_slice.drop(drop_position)
                cave_slice.sand.add(p)
            except SandOverFlow:
                return c
        return -1

    @staticmethod
    def _get_cave_slice(data: Generator[str, None, None]) -> CaveSlice:
        cave_slice = CaveSlice()
        for line in data:
            pairs = line.replace("->", "#").split("#")
            prev_x, prev_y = map(int, pairs[0].split(","))
            for pair in pairs[1:]:
                x, y = map(int, pair.split(","))
                if prev_x == x:
                    for pos_y in range(min(prev_y, y), max(prev_y + 1, y + 1)):
                        cave_slice.rocks.add(CavePosition(x, pos_y))
                else:
                    for pos_x in range(min(prev_x, x), max(prev_x + 1, x + 1)):
                        cave_slice.rocks.add(CavePosition(pos_x, y))
                prev_x, prev_y = x, y

        return cave_slice
