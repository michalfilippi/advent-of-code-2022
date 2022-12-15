from typing import Generator, Union

from base_solution import BaseSolution, TaskInput


class SolutionDay08A(BaseSolution):

    INPUTS = {
        "test": TaskInput(
            file_name="day_08_test.txt",
            result=21,
        ),
        "puzzle": TaskInput(
            file_name="day_08_puzzle.txt",
            result=1717,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        tree_map = self._get_map(data)
        self.logger.info(f"Received tree map {len(tree_map[0])}x{len(tree_map)}.")
        count = 0
        rows = len(tree_map)
        columns = len(tree_map[0])
        for row in range(rows):
            for column in range(columns):
                if any(
                    [
                        self._is_visible(row, column, d_row, d_column, tree_map)
                        for d_row, d_column in [
                            (1, 0),
                            (-1, 0),
                            (0, 1),
                            (0, -1),
                        ]
                    ]
                ):
                    count += 1

        return count

    @staticmethod
    def _is_visible(
        row: int,
        column: int,
        d_row: int,
        d_column: int,
        tree_map: list[list[int]],
    ) -> bool:
        r = row + d_row
        c = column + d_column
        while (0 <= r < len(tree_map)) and (0 <= c < len(tree_map[0])):
            if tree_map[r][c] >= tree_map[row][column]:
                return False
            r = r + d_row
            c = c + d_column
        return True

    @staticmethod
    def _get_map(data: Generator[str, None, None]) -> list[list[int]]:
        return [[int(n) for n in row] for row in data]
