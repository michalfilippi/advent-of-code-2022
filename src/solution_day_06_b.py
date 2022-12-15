from base_solution import TaskInput
from solution_day_06_a import SolutionDay06A


class SolutionDay06B(SolutionDay06A):

    INPUTS = {
        "test": TaskInput(
            file_name="day_06_test.txt",
            result=19,
        ),
        "puzzle": TaskInput(
            file_name="day_06_puzzle.txt",
            result=3298,
        ),
    }

    SEGMENT_LENGTH = 14
