from typing import Generator, Union

from base_solution import TaskInput
from solution_day_01_a import SolutionDay01A


class SolutionDay01B(SolutionDay01A):

    INPUTS = {
        "test": TaskInput(
            file_name="day_01_test.txt",
            result=45000,
        ),
        "puzzle": TaskInput(
            file_name="day_01_puzzle.txt",
            result=195292,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        return sum(sorted(self.get_calories(data))[-3:])
