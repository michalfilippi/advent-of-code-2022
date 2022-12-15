from typing import Generator, Union

from base_solution import BaseSolution, TaskInput


class SolutionDay04A(BaseSolution):

    INPUTS = {
        "test": TaskInput(
            file_name="day_04_test.txt",
            result=2,
        ),
        "puzzle": TaskInput(
            file_name="day_04_puzzle.txt",
            result=513,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        score = 0
        for pair in data:
            first, second = pair.split(",")
            s1, e1 = map(int, first.split("-"))
            s2, e2 = map(int, second.split("-"))
            if (s1 <= s2 and e1 >= e2) or (s1 >= s2 and e1 <= e2):
                score += 1

        return score
