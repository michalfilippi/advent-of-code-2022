from itertools import count
from typing import Generator, Union

from base_solution import TaskInput
from solution_day_14_a import CavePosition, SandOverFlow, SolutionDay14A


class SolutionDay14B(SolutionDay14A):

    INPUTS = {
        "test": TaskInput(
            file_name="day_14_test.txt",
            result=93,
        ),
        "puzzle": TaskInput(
            file_name="day_14_puzzle.txt",
            result=30367,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        cave_slice = self._get_cave_slice(data)
        cave_slice.hard_bottom_offset = 2
        drop_position = CavePosition(500, 0)
        for c in count(1):
            try:
                p = cave_slice.drop(drop_position)
                if p == drop_position:
                    return c
                cave_slice.sand.add(p)
            except SandOverFlow:
                return -1

        raise ValueError("Never reached Sand Overflow")
