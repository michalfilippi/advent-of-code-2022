from typing import Generator, Union

from base_solution import TaskInput
from solution_day_16_a import SolutionDay16A


class SolutionDay16B(SolutionDay16A):

    INPUTS = {
        "test": TaskInput(
            file_name="day_16_test.txt",
            result=56000011,
        ),
        "puzzle": TaskInput(
            file_name="day_16_puzzle.txt",
            result=11756174628223,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        return -1
