from base_solution import TaskInput
from solution_day_05_a import SolutionDay05A


class SolutionDay05B(SolutionDay05A):

    INPUTS = {
        "test": TaskInput(
            file_name="day_05_test.txt",
            result="MCD",
        ),
        "puzzle": TaskInput(
            file_name="day_05_puzzle.txt",
            result="RGLVRCQSB",
        ),
    }

    @staticmethod
    def handle_move(
        stacks: list[list[str]],
        count: int,
        origin: int,
        destination: int,
    ) -> None:
        stacks[destination - 1].extend(stacks[origin - 1][-count:])
        del stacks[origin - 1][-count:]
