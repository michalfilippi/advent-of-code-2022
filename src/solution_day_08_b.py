from math import prod
from typing import Generator, Union

from base_solution import TaskInput
from solution_day_08_a import SolutionDay08A


class SolutionDay08B(SolutionDay08A):

    INPUTS = {
        "test": TaskInput(
            file_name="day_08_test.txt",
            result=8,
        ),
        "puzzle": TaskInput(
            file_name="day_08_puzzle.txt",
            result=321975,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        tree_map = self._get_map(data)
        self.logger.info(f"Received tree map {len(tree_map[0])}x{len(tree_map)}.")
        score = 0
        for row in range(len(tree_map)):
            for column in range(len(tree_map[0])):
                current_score = prod(
                    [
                        self._score(row, column, d_row, d_column, tree_map)
                        for d_row, d_column in [
                            (1, 0),
                            (-1, 0),
                            (0, 1),
                            (0, -1),
                        ]
                    ]
                )
                score = current_score if current_score > score else score

        return score

    @staticmethod
    def _score(
        row: int,
        column: int,
        d_row: int,
        d_column: int,
        tree_map: list[list[int]],
    ) -> int:
        r = row + d_row
        c = column + d_column
        count = 0
        while (0 <= r < len(tree_map)) and (0 <= c < len(tree_map[0])):
            count += 1
            if tree_map[r][c] >= tree_map[row][column]:
                break
            r = r + d_row
            c = c + d_column
        return count
