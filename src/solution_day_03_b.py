from typing import Generator, Union

from base_solution import TaskInput
from solution_day_03_a import SolutionDay03A


class SolutionDay03B(SolutionDay03A):

    INPUTS = {
        "test": TaskInput(
            file_name="day_03_test.txt",
            result=70,
        ),
        "puzzle": TaskInput(
            file_name="day_03_puzzle.txt",
            result=2552,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        score = 0
        rucksacks = []
        for rucksack in data:
            rucksacks.append(set(rucksack))
            if len(rucksacks) == 3:
                common_items = set.intersection(*rucksacks)
                if len(common_items) != 1:
                    raise AssertionError
                common_item = next(iter(common_items))
                score += self.scores[common_item]
                rucksacks = []

        return score
