from typing import Generator, Union

from base_solution import TaskInput
from solution_day_07_a import SolutionDay07A


class SolutionDay07B(SolutionDay07A):

    INPUTS = {
        "test": TaskInput(
            file_name="day_07_test.txt",
            result=24933642,
        ),
        "puzzle": TaskInput(
            file_name="day_07_puzzle.txt",
            result=2877389,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        root = self.get_fs(data)
        sizes = dict(root.dir_sizes())
        to_free = sizes["/"] - (70000000 - 30000000)
        self.logger.info(f"{to_free=}")

        return min(v for v in sizes.values() if v >= to_free)
