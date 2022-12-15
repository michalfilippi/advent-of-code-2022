from typing import Generator, Union

from base_solution import BaseSolution, TaskInput


class SolutionDay10A(BaseSolution):

    INPUTS = {
        "test": TaskInput(
            file_name="day_10_test.txt",
            result=13140,
        ),
        "puzzle": TaskInput(
            file_name="day_10_puzzle.txt",
            result=14420,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        signal_strength = 0
        for i, x in enumerate(self._get_value_x(data)):
            cycle = i + 1
            if (cycle - 20) % 40 == 0:
                signal_strength += cycle * x
        return signal_strength

    @staticmethod
    def _get_value_x(data: Generator[str, None, None]) -> Generator[int, None, None]:
        x = 1
        for row in data:
            parts = row.split()
            match parts[0]:
                case "noop":
                    cycles = 1
                    v = 0
                case "addx":
                    v = int(parts[1])
                    cycles = 2
                case _:
                    raise ValueError(parts)
            for _ in range(cycles):
                yield x
            x += v
