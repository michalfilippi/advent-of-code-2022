from collections import deque
from typing import Generator, Union

from base_solution import BaseSolution, TaskInput


class SolutionDay06A(BaseSolution):

    INPUTS = {
        "test": TaskInput(
            file_name="day_06_test.txt",
            result=7,
        ),
        "puzzle": TaskInput(
            file_name="day_06_puzzle.txt",
            result=1929,
        ),
    }

    SEGMENT_LENGTH = 4

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        message = next(iter(data))
        buffer: deque[str] = deque()
        for i, c in enumerate(message):
            buffer.append(c)
            if len(buffer) == self.SEGMENT_LENGTH:
                if len(set(buffer)) == self.SEGMENT_LENGTH:
                    return i + 1
                buffer.popleft()

        return -1
