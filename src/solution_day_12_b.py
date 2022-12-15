from typing import Generator, Union

from base_solution import TaskInput
from solution_day_12_a import SolutionDay12A


class SolutionDay12B(SolutionDay12A):

    INPUTS = {
        "test": TaskInput(
            file_name="day_12_test.txt",
            result=29,
        ),
        "puzzle": TaskInput(
            file_name="day_12_puzzle.txt",
            result=465,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        heightmap, _, end_position = self._get_heightmap(data)
        return self._get_path(
            heightmap,
            end_position,
            set(heightmap.find_positions(0)),
            reverse=True,
        )
