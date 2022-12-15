from functools import cmp_to_key
from typing import Generator, Union

from base_solution import TaskInput
from solution_day_13_a import SolutionDay13A


class SolutionDay13B(SolutionDay13A):

    INPUTS = {
        "test": TaskInput(
            file_name="day_13_test.txt",
            result=140,
        ),
        "puzzle": TaskInput(
            file_name="day_13_puzzle.txt",
            result=27690,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        sep_1 = [[2]]
        sep_2 = [[6]]
        packets = [sep_1, sep_2]
        score = 1
        for packet_a, packet_b in self._get_pairs(data):
            packets.append(packet_a)
            packets.append(packet_b)

        packets = sorted(packets, key=cmp_to_key(self.compare))

        for i, p in enumerate(packets):
            if p in (sep_1, sep_2):
                score *= i + 1

        return score

    @staticmethod
    def compare(packet_a: list, packet_b: list) -> int:  # type: ignore
        v = SolutionDay13B.is_sorted(packet_a, packet_b)
        if v is None:
            return 0
        elif v:
            return -1
        else:
            return 1
