from typing import Tuple, List

DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1

cur_coordinates = ()

def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""

    grid = grid.strip().splitlines()

    if start_coordinates is None:
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1' and 0 < col < len(grid[row]) - 1:
                    if grid[row][col - 1] == ' ' and grid[row][col + 1] == ' ':
                        start_coordinates = (row, col)

    global cur_coordinates
    cur_coordinates = start_coordinates
    cur_direction = RIGHT
    num = 1
    while True:
        print(num, end="")

        next_direction = find_next_direction(grid, num + 1, cur_direction)

        if next_direction is None:
            break

        print(" ", end="")
        if next_direction != cur_direction:
            print(next_direction)

        num += 1
        cur_direction = next_direction


def find_next_direction(grid, next_num: int, cur_direction=RIGHT) -> str | None:
    global cur_coordinates
    row: int = cur_coordinates[0]
    col: int = cur_coordinates[1]

    if find_next_num_right(grid, row, col, next_num):
        return RIGHT
    if find_next_num_down(grid, row, col, next_num):
        return DOWN
    if find_next_num_left(grid, row, col, next_num):
        return LEFT
    if find_next_num_up(grid, row, col, next_num):
        return UP

    return None

def find_next_num_right(grid, row: int, col: int, next_num: int) -> bool:
    global cur_coordinates
    if len(grid[row]) <= col + 5:
        return False
    if grid[row][col + 2] == '-':
        next_num_str = (grid[row][col + 4] + grid[row][col + 5]).strip()
        if next_num_str == str(next_num):
            cur_coordinates = (row, col + 5)
            return True
    return False

def find_next_num_down(grid, row: int, col: int, next_num: int) -> bool:
    global cur_coordinates
    if len(grid) <= row + 2 or len(grid[row + 1]) <= col or len(grid[row + 2]) <= col:
        return False
    if grid[row + 1][col] == '|':
        next_num_str = (grid[row + 2][col - 1] + grid[row + 2][col]).strip()
        if next_num_str == str(next_num):
            cur_coordinates = (row + 2, col)
            return True
    return False

def find_next_num_left(grid, row: int, col: int, next_num: int) -> bool:
    global cur_coordinates
    if col - 6 < 0:
        return False
    if grid[row][col - 3] == '-':
        next_num_str = (grid[row][col - 6] + grid[row][col - 5]).strip()
        if next_num_str == str(next_num):
            cur_coordinates = (row, col - 5)
            return True
    return False

def find_next_num_up(grid, row: int, col: int, next_num: int) -> bool:
    global cur_coordinates
    if row - 2 < 0 or len(grid[row - 1]) <= col or len(grid[row - 2]) <= col:
        return False
    if grid[row - 1][col] == '|':
        next_num_str = (grid[row - 2][col - 1] + grid[row - 2][col]).strip()
        if next_num_str == str(next_num):
            cur_coordinates = (row - 2, col)
            return True
    return False


if __name__ == '__main__':
    small_grid = """
    21 - 22 - 23 - 24 - 25
     |
    20    7 -  8 -  9 - 10
     |    |              |
    19    6    1 -  2   11
     |    |         |    |
    18    5 -  4 -  3   12
     |                   |
    17 - 16 - 15 - 14 - 13
    """

    print_sequence_route(small_grid)