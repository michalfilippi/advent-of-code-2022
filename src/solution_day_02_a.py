from typing import Generator, Union

from base_solution import BaseSolution, TaskInput


class SolutionDay02A(BaseSolution):

    INPUTS = {
        "test": TaskInput(
            file_name="day_02_test.txt",
            result=15,
        ),
        "puzzle": TaskInput(
            file_name="day_02_puzzle.txt",
            result=15632,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        score = 0
        for opponent_move, move in self.get_rounds(data):
            match (opponent_move, move):
                case ("A", "X"):
                    score += 3 + 1
                case ("A", "Y"):
                    score += 6 + 2
                case ("A", "Z"):
                    score += 0 + 3
                case ("B", "X"):
                    score += 0 + 1
                case ("B", "Y"):
                    score += 3 + 2
                case ("B", "Z"):
                    score += 6 + 3
                case ("C", "X"):
                    score += 6 + 1
                case ("C", "Y"):
                    score += 0 + 2
                case ("C", "Z"):
                    score += 3 + 3
        return score

    @staticmethod
    def get_rounds(
        data: Generator[str, None, None]
    ) -> Generator[tuple[str, str], None, None]:
        for line in data:
            if line != "":
                a, b = line.split()
                yield a, b
