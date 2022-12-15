from abc import ABC, abstractmethod
from dataclasses import dataclass
from logging import getLogger
from typing import Generator, Optional, Union


@dataclass
class TaskInput:
    file_name: str
    result: Optional[Union[int, str]] = None
    extra_params: Optional[dict[str, Union[str, int]]] = None

    def get_extra_params(self) -> dict[str, Union[str, int]]:
        return {} if self.extra_params is None else self.extra_params


class BaseSolution(ABC):

    INPUTS: dict[str, TaskInput] = dict()

    def __init__(self) -> None:
        self.logger = getLogger(__name__)

    def solve(
        self,
        input_file: str,
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        return self._solve(self._read_file(input_file), extra_params)

    @abstractmethod
    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        pass

    @staticmethod
    def _read_file(file_name: str) -> Generator[str, None, None]:
        with open(file_name, "r") as f_in:
            for line in f_in:
                if line.endswith("\n"):
                    yield line[:-1]
                else:
                    yield line
