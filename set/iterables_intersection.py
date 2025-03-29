import functools
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    args = [list(arg) for arg in args if arg is not None]
    args = [arg for arg in args if 0 < len(arg)]

    if len(args) == 0:
        return set()

    if len(args) == 1:
        return set(args[0])

    results = []
    for item in args[0]:
        common_item = True
        for i in range(1, len(args)):
            if item not in args[i]:
                common_item = False
                break
        if common_item:
            results.append(item)

    return set(results)