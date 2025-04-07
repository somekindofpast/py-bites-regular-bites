import typer
from rich.console import Console
from rich.table import Table


app = typer.Typer()
console = Console()

@app.command()
def table():
    tool_table = Table("Name", "Favorite Tool/Framework")
    tool_table.add_row("Bob", "Vim")
    tool_table.add_row("Julian", "Flask")
    tool_table.add_row("Robin", "VS Code")
    console.print(tool_table)


if __name__ == "__main__":
    app()