from typing import Generator, Union

from base_solution import BaseSolution, TaskInput


class SolutionDay16A(BaseSolution):

    INPUTS = {
        "test": TaskInput(
            file_name="day_16_test.txt",
            result=26,
        ),
        "puzzle": TaskInput(
            file_name="day_16_puzzle.txt",
            result=5525990,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        return 0
