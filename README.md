# Advent of Code 2022 🎄

[Advent of Code 2022](https://adventofcode.com/) solutions in Python.

## Requirements ⚒

The solutions are intended for Python 3.11, although the majority of the solutions should work even with older versions of Python. Required Python packages are specified in [requirements.txt](requirements.txt). Use `pip` to install them.

```shell
pip install -r requirements.txt
```

## Running Solutions 🏃

The repository contains a [script](src/main.py)  designed for running solutions and comparing expected result with produced result. To use it, navigate first to the `src` directory inside the project repository.

```shell
cd src
```

You can get the script help using `--help` parameter.


```shell
python main.py --help
```

There are two required parameters to specify which solution should be executed. To run solution for day `6` part `a`, use the following command.  


```shell
python main.py 6 a
```

To select a different input for the solution, use option `--task-input`. The default value is `test`. To execute solution with actual puzzle input the following command.


```shell
python main.py 6 a --task-input puzzle
```

The command should result the following output.

```text
INFO:2022-12-15 18:42:05,327:__main__:Running day_str='06' task='a' task_input='test'
INFO:2022-12-15 18:42:05,327:__main__:Importing solution module.
INFO:2022-12-15 18:42:05,328:__main__:Accessing solution class.
INFO:2022-12-15 18:42:05,328:__main__:Creating a solution instance.
INFO:2022-12-15 18:42:05,328:__main__:Running solution for /path_to_repository/advent-of-code-2022/src/inputs/day_06_test.txt
INFO:2022-12-15 18:42:05,328:pytimers.triggers.logger_trigger:Finished task run in 0.053ms [0.0s].
INFO:2022-12-15 18:42:05,328:__main__:Result: 7
INFO:2022-12-15 18:42:05,328:__main__:Expected result: 7
INFO:2022-12-15 18:42:05,328:__main__:Success!!

```

## Disclaimer 🎁

The solutions were optimized for implementation speed (I didn't want to finish last obviously 🐢) with reasonable focus on code quality on the other hand. Therefore, solutions are by no means optimal and there should be cleaner and faster solutions around.