from typing import Generator, Union

from base_solution import TaskInput
from solution_day_10_a import SolutionDay10A


class SolutionDay10B(SolutionDay10A):

    INPUTS = {
        "test": TaskInput(
            file_name="day_10_test.txt",
        ),
        "puzzle": TaskInput(
            file_name="day_10_puzzle.txt",
            result="RGLRBZAU",
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        line: list[str] = []
        for x in self._get_value_x(data):
            pos = len(line)
            if pos in [x - 1, x, x + 1]:
                line.append("#")
            else:
                line.append(".")
            if len(line) == 40:
                self.logger.info("".join(line))
                line = []

        # the actual answer to this task depends on the ASCII art in the output
        return 0
