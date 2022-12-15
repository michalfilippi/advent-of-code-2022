from typing import Generator, Union

from base_solution import BaseSolution, TaskInput


class SolutionDay01A(BaseSolution):

    INPUTS = {
        "test": TaskInput(
            file_name="day_01_test.txt",
            result=24000,
        ),
        "puzzle": TaskInput(
            file_name="day_01_puzzle.txt",
            result=66306,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        return max(self.get_calories(data))

    @staticmethod
    def get_calories(data: Generator[str, None, None]) -> list[int]:
        calories = []
        tmp_sum = 0
        for item in data:
            if item == "":
                calories.append(tmp_sum)
                tmp_sum = 0
            else:
                tmp_sum += int(item)
        calories.append(tmp_sum)
        return calories
