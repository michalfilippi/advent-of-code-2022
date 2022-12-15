import string
from typing import Generator, Union

import parse  # type: ignore

from base_solution import BaseSolution, TaskInput


class SolutionDay05A(BaseSolution):

    INPUTS = {
        "test": TaskInput(
            file_name="day_05_test.txt",
            result="CMZ",
        ),
        "puzzle": TaskInput(
            file_name="day_05_puzzle.txt",
            result="SBPQRSCDF",
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        stacks = self.parse_stacks(data)
        for move_str in data:
            format_string = "move {:d} from {:d} to {:d}"
            count, origin, destination = parse.parse(format_string, move_str).fixed
            self.handle_move(stacks, count, origin, destination)
        return "".join(s[-1] for s in stacks)

    @staticmethod
    def handle_move(
        stacks: list[list[str]],
        count: int,
        origin: int,
        destination: int,
    ) -> None:
        for _ in range(count):
            e = stacks[origin - 1].pop()
            stacks[destination - 1].append(e)

    @staticmethod
    def parse_stacks(data: Generator[str, None, None]) -> list[list[str]]:
        stacks: list[list[str]] = []
        for line in data:
            if line == "":
                return [s[::-1] for s in stacks]
            elif "[" in line:
                if len(stacks) == 0:
                    for _ in range((len(line) + 1) // 4):
                        stacks.append([])
                for stack, pos in enumerate(range(0, len(line), 4)):
                    for x in line[pos : pos + 4]:
                        if x in string.ascii_uppercase:
                            stacks[stack].append(x)

        raise ValueError("Missing empty line at the end of the input.")
