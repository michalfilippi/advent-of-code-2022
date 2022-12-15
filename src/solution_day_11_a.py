from math import floor, prod
from typing import Generator, Union

from base_solution import BaseSolution, TaskInput


class Monkey:
    def __init__(
        self,
        items: list[int],
        multiplication_constant: int,
        addition_constant: int,
        power_constant: int,
        modulo_constant: int,
        monkey_true: int,
        monkey_false: int,
    ):
        self.items = items
        self.multiplication_constant = multiplication_constant
        self.addition_constant = addition_constant
        self.power_constant = power_constant
        self.modulo_constant = modulo_constant
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false
        self.inspection_counter = 0

    def turn(
        self,
        worry_level_division: int,
    ) -> Generator[tuple[int, int], None, None]:
        for item in self.items:
            self.inspection_counter += 1
            new_val = floor(
                (item**self.power_constant + self.addition_constant)
                * self.multiplication_constant
                / worry_level_division
            )
            if (new_val % self.modulo_constant) == 0:
                yield new_val, self.monkey_true
            else:
                yield new_val, self.monkey_false
        self.items = []


class SolutionDay11A(BaseSolution):

    INPUTS = {
        "test": TaskInput(
            file_name="day_11_test.txt",
            result=10605,
        ),
        "puzzle": TaskInput(
            file_name="day_11_puzzle.txt",
            result=56595,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        monkeys = self._get_monkeys(data)
        for _ in range(20):
            for monkey in monkeys:
                for item, monkey_id in monkey.turn(3):
                    monkeys[monkey_id].items.append(item)
        counters = [monkey.inspection_counter for monkey in monkeys]
        return prod(sorted(counters)[-2:])

    @staticmethod
    def _get_monkeys(data: Generator[str, None, None]) -> list[Monkey]:
        monkeys = []
        while True:
            try:
                _ = next(data)
                items = list(map(int, next(data).split(":")[1].split(",")))

                operation_o, operation_c = next(data).split()[-2:]
                if operation_o == "+":
                    multiplication_constant = 1
                    power_constant = 1
                    addition_constant = int(operation_c)
                else:
                    if operation_c == "old":
                        multiplication_constant = 1
                        power_constant = 2
                        addition_constant = 0
                    else:
                        multiplication_constant = int(operation_c)
                        addition_constant = 0
                        power_constant = 1
                modulo_constant = int(next(data).split()[-1])

                monkey_true = int(next(data).split()[-1])
                monkey_false = int(next(data).split()[-1])

                monkeys.append(
                    Monkey(
                        items,
                        multiplication_constant,
                        addition_constant,
                        power_constant,
                        modulo_constant,
                        monkey_true,
                        monkey_false,
                    )
                )

                _ = next(data)
            except StopIteration:
                break
        return monkeys
