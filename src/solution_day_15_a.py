from math import fabs
from typing import Generator, Union

import parse  # type: ignore

from base_solution import BaseSolution, TaskInput
from common import Position


class SolutionDay15A(BaseSolution):

    INPUTS = {
        "test": TaskInput(
            file_name="day_15_test.txt",
            result=26,
            extra_params={
                "line_y": 10,
            },
        ),
        "puzzle": TaskInput(
            file_name="day_15_puzzle.txt",
            result=5525990,
            extra_params={
                "line_y": 2000000,
            },
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        line_y = int(extra_params["line_y"])
        no_sensor_segments = []
        for sensor, beacon in self._parse_input(data):
            distance = sensor.manhattan_distance(beacon)
            length = distance - round(fabs(sensor.y - line_y))
            if length >= 0:
                if beacon.y == line_y and sensor.x - length == beacon.x:
                    start = sensor.x - length + 1
                else:
                    start = sensor.x - length
                if beacon.y == line_y and sensor.x + length == beacon.x:
                    end = sensor.x + length - 1
                else:
                    end = sensor.x + length
                if start <= end:
                    no_sensor_segments.append((start, end))

        disjoint_segments = self._join_segments(no_sensor_segments)

        return sum(e - s + 1 for s, e in disjoint_segments)

    @staticmethod
    def _parse_input(
        data: Generator[str, None, None],
    ) -> Generator[tuple[Position, Position], None, None]:
        format_string = "Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}"
        for line in data:
            s_x, s_y, b_x, b_y = parse.parse(format_string, line).fixed
            yield Position(s_x, s_y), Position(b_x, b_y)

    @staticmethod
    def _join_segments(segments: list[tuple[int, int]]) -> list[tuple[int, int]]:
        disjoint_segments = []
        sorted_segments = sorted(segments)
        current_start, current_end = sorted_segments[0]
        for start, end in sorted_segments[1:]:
            if start <= current_end + 1:
                current_end = max(end, current_end)
            else:
                disjoint_segments.append((current_start, current_end))
                current_start = start
                current_end = end
        disjoint_segments.append((current_start, current_end))

        return disjoint_segments
