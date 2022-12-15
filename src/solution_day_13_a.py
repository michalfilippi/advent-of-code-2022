from ast import literal_eval
from typing import Generator, Optional, Union

from base_solution import BaseSolution, TaskInput


class SolutionDay13A(BaseSolution):

    INPUTS = {
        "test": TaskInput(
            file_name="day_13_test.txt",
            result=13,
        ),
        "puzzle": TaskInput(
            file_name="day_13_puzzle.txt",
            result=5529,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        counter = 0
        for i, (packet_a, packet_b) in enumerate(self._get_pairs(data)):
            if self.is_sorted(packet_a, packet_b):
                counter += i + 1
        return counter

    @staticmethod
    def _get_pairs(
        data: Generator[str, None, None]
    ) -> Generator[tuple[list, list], None, None]:  # type: ignore
        packets: list[list] = []  # type: ignore
        for line in data:
            if line == "" and packets:
                yield packets[0], packets[1]
                packets = []
            else:
                packets.append(literal_eval(line))
        yield packets[0], packets[1]

    @staticmethod
    def is_sorted(packet_a: list, packet_b: list) -> Optional[bool]:  # type: ignore
        for a, b in zip(packet_a, packet_b):
            if type(a) == type(b) == int:
                if a < b:
                    return True
                elif a > b:
                    return False
            elif type(a) == int:
                nested_result = SolutionDay13A.is_sorted([a], b)
                if nested_result is not None:
                    return nested_result
            elif type(b) == int:
                nested_result = SolutionDay13A.is_sorted(a, [b])
                if nested_result is not None:
                    return nested_result
            else:
                nested_result = SolutionDay13A.is_sorted(a, b)
                if nested_result is not None:
                    return nested_result

        if len(packet_a) < len(packet_b):
            return True
        elif len(packet_a) > len(packet_b):
            return False
        else:
            return None
