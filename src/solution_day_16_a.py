from dataclasses import dataclass
from typing import Generator, Optional, Iterable, Union

import parse  # type: ignore

from base_solution import BaseSolution, TaskInput


@dataclass(frozen=True)
class Action:
    pass


@dataclass(frozen=True)
class Move(Action):
    from_valve: str
    to_valve: str


@dataclass(frozen=True)
class Open(Action):
    valve: str


@dataclass(frozen=True)
class Valve:
    name: str
    rate: int
    tunnels: set[str]

    def moves(self) -> Generator[Move, None, None]:
        for tunnel in self.tunnels:
            yield Move(self.name, tunnel)


class SolutionDay16A(BaseSolution):

    INPUTS = {
        "test": TaskInput(
            file_name="day_16_test.txt",
            result=1651,
        ),
        "puzzle": TaskInput(
            file_name="day_16_puzzle.txt",
            result=-1,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        start_valve = "AA"
        valves = self._get_valves(data)
        max_actions = 30
        actions = self.find_actions(valves, start_valve, max_actions)
        self.logger.info(f"Best actions {actions}")
        return self._score_actions(actions, valves, max_actions)

    @staticmethod
    def _get_valves(
        data: Generator[str, None, None],
    ) -> dict[str, Valve]:
        format_string = "Valve {name} has flow rate={rate:d}; {t} to {v} {tunnels}"
        valves: dict[str, Valve] = {}
        for line in data:
            parsed_values = parse.parse(format_string, line)
            name = parsed_values["name"]
            rate = parsed_values["rate"]
            tunnels = {
                s.strip()
                for s in parsed_values["tunnels"].split(",")
            }
            valves[name] = Valve(name, rate, tunnels)
        return valves

    @staticmethod
    def _score_actions_to_last_open(
        actions: Iterable[Action],
        valves: dict[str, Valve],
    ) -> int:
        score = 0
        global_rate = 0
        last_step = 0
        for step, rate in [
            (i + 1, valves[action.valve].rate)
            for i, action in enumerate(actions)
            if isinstance(action, Open)
        ]:
            score += (step - last_step) * global_rate
            global_rate += rate
        return score

    @staticmethod
    def _score_actions(
        actions: Iterable[Action],
        valves: dict[str, Valve],
        max_actions: int,
    ) -> int:
        global_rate = 0
        score = 0
        length = 0
        for action in actions:
            length += 1
            if length > max_actions:
                break
            score += global_rate
            match action:
                case Open(valve):
                    global_rate += valves[valve].rate
        for _ in range(length, max_actions):
            score += global_rate

        return score

    def find_actions(
        self,
        valves: dict[str, Valve],
        start_valve: str,
        max_actions: int,
    ) -> Optional[tuple[Action]]:
        current_actions = []
        max_score = 0
        best_actions: Optional[tuple[Action]] = None
        for actions in self._find_actions(
            valves,
            start_valve,
            current_actions,
            set(),
            dict(),
            max_actions,
        ):
            # self.logger.info(f"Yielded {self._score_actions(actions, valves)=} {actions}")
            score = self._score_actions(actions, valves, max_actions)
            if score > max_score:
                # self.logger.info(f"IMPROVED: {score=} {actions}")
                best_actions = tuple(actions)
                max_score = score

        return best_actions

    def _find_actions(
        self,
        valves: dict[str, Valve],
        current_valve: str,
        current_actions: list[Action],
        open_valves: set[str],
        visited: dict[tuple[str, frozenset[str], int], int],
        max_actions: int,
    ) -> Generator[list[Action], None, None]:
        # self.logger.info(
        #     f"{current_valve=} {len(current_actions)=} {current_actions=} {open_valves=}"
        # )
        state = (
            current_valve,
            frozenset(open_valves),
            self._score_actions_to_last_open(current_actions, valves),
        )
        if state in visited and visited[state] <= len(current_actions):
            return
        else:
            if current_actions and isinstance(current_actions[-1], Open):
                yield current_actions
            visited[state] = len(current_actions)

        if len(current_actions) < max_actions:
            if current_valve not in open_valves and valves[current_valve].rate > 0:
                yield from self._find_actions(
                    valves,
                    current_valve,
                    current_actions + [Open(current_valve)],
                    open_valves | {current_valve},
                    visited,
                    max_actions,
                )
            for next_valve in valves[current_valve].tunnels:
                yield from self._find_actions(
                    valves,
                    next_valve,
                    current_actions + [Move(current_valve, next_valve)],
                    open_valves,
                    visited,
                    max_actions,
                )
