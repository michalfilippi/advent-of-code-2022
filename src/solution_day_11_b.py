from math import prod
from typing import Generator, Union

from base_solution import TaskInput
from solution_day_11_a import SolutionDay11A


class SolutionDay11B(SolutionDay11A):

    INPUTS = {
        "test": TaskInput(
            file_name="day_11_test.txt",
            result=2713310158,
        ),
        "puzzle": TaskInput(
            file_name="day_11_puzzle.txt",
            result=15693274740,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        monkeys = self._get_monkeys(data)
        common = prod(monkey.modulo_constant for monkey in monkeys)
        for _ in range(10000):
            for monkey in monkeys:
                for item, monkey_id in monkey.turn(1):
                    monkeys[monkey_id].items.append(item % common)
        counters = [monkey.inspection_counter for monkey in monkeys]
        return prod(sorted(counters)[-2:])
