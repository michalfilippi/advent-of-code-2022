from math import fabs
from typing import Generator, Union

from base_solution import TaskInput
from solution_day_15_a import SolutionDay15A


class SolutionDay15B(SolutionDay15A):

    INPUTS = {
        "test": TaskInput(
            file_name="day_15_test.txt",
            result=56000011,
            extra_params={
                "min_x": 0,
                "max_x": 20,
                "min_y": 0,
                "max_y": 20,
            },
        ),
        "puzzle": TaskInput(
            file_name="day_15_puzzle.txt",
            result=11756174628223,
            extra_params={
                "min_x": 0,
                "max_x": 4000000,
                "min_y": 0,
                "max_y": 4000000,
            },
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        input_data = list(self._parse_input(data))
        min_x, max_x = int(extra_params["min_x"]), int(extra_params["max_x"])
        min_y, max_y = int(extra_params["min_y"]), int(extra_params["max_y"])
        for line_y in range(min_y, max_y + 1):
            no_sensor_segments = []
            for sensor, beacon in input_data:
                distance = sensor.manhattan_distance(beacon)
                length = distance - round(fabs(sensor.y - line_y))
                if length >= 0:
                    start = max(sensor.x - length, min_x)
                    end = min(sensor.x + length, max_x)
                    if start <= end:
                        no_sensor_segments.append((start, end))

            disjoint_segments = self._join_segments(no_sensor_segments)
            total = sum(e - s + 1 for s, e in disjoint_segments)
            if total <= max_x:
                self.logger.info(f"{line_y} {total=} {disjoint_segments=}")
                if len(disjoint_segments) == 2:
                    return (disjoint_segments[0][1] + 1) * 4000000 + line_y
                elif disjoint_segments[0][0] == 0:
                    return max_x * 4000000 + line_y
                else:
                    return line_y

        return -1
