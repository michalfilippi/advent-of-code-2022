from typing import Generator, Union

from base_solution import TaskInput
from solution_day_09_a import RopePosition, SolutionDay09A


class SolutionDay09B(SolutionDay09A):

    INPUTS = {
        "test": TaskInput(
            file_name="day_09_test.txt",
            result=1,
        ),
        "puzzle": TaskInput(
            file_name="day_09_puzzle.txt",
            result=2443,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        positions = [RopePosition(0, 0) for _ in range(10)]
        visited = set()

        for line in data:
            direction, count_str = line.split()
            count = int(count_str)
            for _ in range(count):
                positions[0] = positions[0].move(direction)
                for i in range(1, len(positions)):
                    positions[i] = positions[i].follow(positions[i - 1])
                visited.add((positions[-1].x, positions[-1].y))

        return len(visited)
