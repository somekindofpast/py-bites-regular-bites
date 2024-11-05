from typing import List

EAST = "E"
WEST = "W"


def search_apartment(buildings: List[int], direction: str) -> List[int]:
    """
    Find and return the indices of those building with
    the desired view: EAST (E) or WEST (W).

    See sample inputs / outputs below and in the tests.
    """

    result: List[int] = []
    count_range = [0, len(buildings), 1] if direction == WEST else [len(buildings) - 1, -1, -1]
    highest: int = buildings[0] if direction == WEST else buildings[-1]
    for i in range(count_range[0], count_range[1], count_range[2]):
        if highest < buildings[i] or (direction == WEST and i == 0) or (direction == EAST and i == len(buildings) - 1):
            if direction == EAST:
                result.insert(0, i)
            else:
                result.append(i)
            highest = buildings[i]
    return result


if __name__ == '__main__':
    print(search_apartment([3, 5, 4, 3, 3, 1], WEST))