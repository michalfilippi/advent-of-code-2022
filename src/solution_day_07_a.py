from dataclasses import dataclass, field
from typing import Generator, Optional, Union

from base_solution import BaseSolution, TaskInput


@dataclass
class Directory:
    name: str
    parent: Optional["Directory"]
    directories: dict[str, "Directory"] = field(default_factory=dict)
    files: dict[str, int] = field(default_factory=dict)

    def size(self) -> int:
        return sum(self.files.values())

    def dir_sizes(self) -> Generator[tuple[str, int], None, int]:
        my_size = 0
        for subdir in self.directories.values():
            subdir_size = yield from subdir.dir_sizes()
            my_size += subdir_size
        my_size += self.size()
        yield self.name, my_size
        return my_size


class SolutionDay07A(BaseSolution):

    INPUTS = {
        "test": TaskInput(
            file_name="day_07_test.txt",
            result=95437,
        ),
        "puzzle": TaskInput(
            file_name="day_07_puzzle.txt",
            result=919137,
        ),
    }

    def _solve(
        self,
        data: Generator[str, None, None],
        extra_params: dict[str, Union[int, str]],
    ) -> Union[int, str]:
        root = self.get_fs(data)
        return sum(v for _, v in root.dir_sizes() if v <= 100_000)

    @staticmethod
    def get_fs(data: Generator[str, None, None]) -> Directory:
        root = Directory(name="/", parent=None)
        current_directory = root
        for line in data:
            parts = line.split()
            if parts[0] == "$":
                if parts[1] == "cd":
                    if parts[2] == "/":
                        current_directory = root
                    elif parts[2] == "..":
                        if current_directory.parent is not None:
                            current_directory = current_directory.parent
                        else:
                            raise ValueError(
                                f"Directory {current_directory} has no parent."
                            )
                    else:
                        current_directory = current_directory.directories[parts[2]]
            elif parts[0] == "dir":
                if parts[1] not in current_directory.directories:
                    current_directory.directories[parts[1]] = Directory(
                        name=parts[1],
                        parent=current_directory,
                    )
            else:
                size = int(parts[0])
                current_directory.files[parts[1]] = size
        return root
