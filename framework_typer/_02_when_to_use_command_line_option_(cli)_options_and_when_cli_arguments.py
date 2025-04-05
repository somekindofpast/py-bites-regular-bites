import typer
from typing_extensions import Annotated


def sum_numbers(a: int, b: int):
    return a + b


def main(
    a: int = typer.Argument(..., help="The value of the first summand"),
    b: int = typer.Argument(..., help="The value of the second summand"),
    c: Annotated[int, typer.Option()] = None
):
    """CLI that allows you to add two numbers"""
    summed_nums = sum_numbers(a, b)
    comparison = None
    if c is not None:
        comparison = "smaller" if c < summed_nums else "not smaller"
    print(f"The sum is {summed_nums} and c is {comparison}")


if __name__ == "__main__":
    typer.run(main)