from typing import Generator, Union

from base_solution import TaskInput
from solution_day_02_a import SolutionDay02A


class SolutionDay02B(SolutionDay02A):

    INPUTS = {
        "test": TaskInput(
            file_name="day_02_test.txt",
            result=12,
        ),
        "puzzle": TaskInput(
            file_name="day_02_puzzle.txt",
            result=14416,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        score = 0
        for opponent_move, outcome in self.get_rounds(data):
            match (opponent_move, outcome):
                case ("A", "X"):
                    score += 0 + 3
                case ("A", "Y"):
                    score += 3 + 1
                case ("A", "Z"):
                    score += 6 + 2
                case ("B", "X"):
                    score += 0 + 1
                case ("B", "Y"):
                    score += 3 + 2
                case ("B", "Z"):
                    score += 6 + 3
                case ("C", "X"):
                    score += 0 + 2
                case ("C", "Y"):
                    score += 3 + 3
                case ("C", "Z"):
                    score += 6 + 1
        return score
