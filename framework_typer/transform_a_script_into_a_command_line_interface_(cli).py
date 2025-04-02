import typer  # use typer.run and typer.Argument
from typing_extensions import Annotated


def sum_numbers(a: int, b: int):
    """Sums two numbers"""
    return a + b


def main(
    a: Annotated[int, typer.Argument()] = "The value of the first summand",
    b: Annotated[int, typer.Argument()] = "The value of the second summand"
):
    """
    CLI that allows you to add two numbers
    """
    print(sum_numbers(a, b))


if __name__ == "__main__":
    typer.run(main)