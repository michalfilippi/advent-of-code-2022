import string
from typing import Generator, Union

from base_solution import BaseSolution, TaskInput


class SolutionDay03A(BaseSolution):

    INPUTS = {
        "test": TaskInput(
            file_name="day_03_test.txt",
            result=157,
        ),
        "puzzle": TaskInput(
            file_name="day_03_puzzle.txt",
            result=8493,
        ),
    }

    scores = {c: i + 1 for i, c in enumerate(string.ascii_letters)}

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        score = 0
        for rucksack in data:
            first_half, second_half = (
                rucksack[: len(rucksack) // 2],
                rucksack[len(rucksack) // 2 :],
            )
            common_item = set(first_half).intersection(set(second_half))
            assert len(common_item) == 1
            item = next(iter(common_item))
            score += self.scores[item]

        return score
