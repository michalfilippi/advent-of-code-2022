import importlib
import logging
from pathlib import Path

import click
import pytimers
from dotenv import load_dotenv

from base_solution import BaseSolution


logging.basicConfig(
    format="%(levelname)s:%(asctime)s:%(name)s:%(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


@click.command()
@click.argument(
    "day",
    type=click.INT,
    envvar="DAY",
)
@click.argument(
    "task",
    type=click.Choice(["a", "b"], case_sensitive=False),
    envvar="TASK",
)
@click.option(
    "--task-input",
    type=str,
    default="test",
    envvar="TASK_INPUT",
)
def cli(
    day: int,
    task: str,
    task_input: str,
) -> None:
    day_str = str(day).zfill(2)
    logger.info(f"Running {day_str=} {task=} {task_input=}")

    solution_path = f"solution_day_{day_str}_{task}"
    solution_class_name = f"SolutionDay{day_str}{task.upper()}"
    logger.info("Importing solution module.")
    try:
        solution_module = importlib.import_module(solution_path)
    except ModuleNotFoundError:
        logger.error(f"Could not import module {solution_path}.")
        return

    logger.info("Accessing solution class.")
    try:
        solution_class: type[BaseSolution] = getattr(
            solution_module,
            solution_class_name,
        )
    except AttributeError:
        logger.error(
            f"Failed to get the solution class {solution_class_name} from solution "
            f"module {solution_module}."
        )
        return

    if task_input not in solution_class.INPUTS:
        logger.error(
            f"Input {task_input} is missing from the Solution.INPUT attribute. "
            f"Available inputs are {', '.join(solution_class.INPUTS.keys())}"
        )
        return
    else:
        task_input_obj = solution_class.INPUTS[task_input]

    file_input = Path(__file__).parent / "inputs" / task_input_obj.file_name

    if file_input.is_file():
        logger.info("Creating a solution instance.")
        solution = solution_class()
        logger.info(f"Running solution for {file_input}")
        with pytimers.timer.label("task run"):
            result = solution.solve(
                str(file_input),
                task_input_obj.get_extra_params(),
            )
    else:
        logger.error(f"Input file {str(file_input)} does not exist.")
        return

    logger.info(f"Result: {result}")

    if solution_class.INPUTS[task_input].result is not None:
        logger.info(f"Expected result: {task_input_obj.result}")

        if result == task_input_obj.result:
            logger.info("Success!!")
        else:
            logger.info("Oh no.")


if __name__ == "__main__":
    load_dotenv()
    cli()
