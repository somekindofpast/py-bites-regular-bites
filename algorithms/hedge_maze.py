from collections import deque
from typing import List, Tuple, Self

OPEN_SPACE = '.'
WALL = '+'
COVERED_SPACE = '!'

class Cell:
    def __init__(self, row: int, col: int, steps: int):
        self.row  = row
        self.col = col
        self.steps = steps

    def get_open_neighbors(self, maze: List[List[str]]) -> List[Self]:
        neighbors: List[Cell] = []

        if 0 < self.row and maze[self.row - 1][self.col] == OPEN_SPACE:
            neighbors.append(Cell(self.row - 1, self.col, self.steps + 1))

        if self.row < len(maze) - 1 and maze[self.row + 1][self.col] == OPEN_SPACE:
            neighbors.append(Cell(self.row + 1, self.col, self.steps + 1))

        if 0 < self.col and maze[self.row][self.col - 1] == OPEN_SPACE:
            neighbors.append(Cell(self.row, self.col - 1, self.steps + 1))

        if self.col < len(maze[self.row]) - 1 and maze[self.row][self.col + 1] == OPEN_SPACE:
            neighbors.append(Cell(self.row, self.col + 1, self.steps + 1))

        return neighbors


def hedge_maze(maze: List[List[str]], entrance: Tuple[int, int]) -> int:
    """Finds the shortest distance from the entrance to the nearest exit in a maze."""
    if (
            entrance[0] < 0 or
            len(maze) <= entrance[0] or
            entrance[1] < 0 or
            len(maze[0]) <= entrance[1] or
            maze[entrance[0]][entrance[1]] != OPEN_SPACE
    ):
        raise ValueError()

    exits = search_exits(maze, entrance)

    queue = deque([Cell(entrance[0], entrance[1], 0)])

    while 0 < len(queue):
        cell: Cell = queue.pop()
        maze[cell.row][cell.col] = COVERED_SPACE
        if (cell.row, cell.col) in exits:
            return cell.steps
        for neighbor in cell.get_open_neighbors(maze):
            queue.appendleft(neighbor)

    return -1


def search_exits(maze: List[List[str]], entrance: Tuple[int, int]) -> List[Tuple[int, int]]:
    exits: List[Tuple[int, int]] = []
    for row in range(len(maze)):
        if row == 0 or row == len(maze) - 1:
            for col in range(len(maze[row])):
                if is_exit(maze, row, col, entrance):
                    exits.append((row, col))
        else:
            col = 0
            if is_exit(maze, row, col, entrance):
                exits.append((row, col))
            col = len(maze[row]) - 1
            if is_exit(maze, row, col, entrance):
                exits.append((row, col))
    return exits


def is_exit(maze: List[List[str]], row: int, col: int, entrance: Tuple[int, int]) -> bool:
    return maze[row][col] == OPEN_SPACE and not (row == entrance[0] and col == entrance[1])


if __name__ == '__main__':
    maze_ = [
        ["+", "+", ".", "."],
        [".", ".", ".", "+"],
        ["+", "+", "+", "+"]
    ]
    print(hedge_maze(maze_, (1, 0)))
    maze_ = [
        ["+", "+", ".", "+"],
        [".", "+", ".", "+"],
        ["+", ".", "+", "+"]
    ]
    print(hedge_maze(maze_, (0, 2)))

    try:
        maze_ = [
            ["+", "+", ".", "+"],
            [".", ".", ".", "+"],
            ["+", "+", "+", "."]
        ]
        print(hedge_maze(maze_, (3, 5)))
    except ValueError:
        print("ValueError")

    try:
        maze_ = [
            ["+", "+", ".", "+"],
            [".", ".", ".", "+"],
            ["+", "+", "+", "."]
        ]
        print(hedge_maze(maze_, (0, 0)))
    except ValueError:
        print("ValueError")