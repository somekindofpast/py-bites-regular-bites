from typing import Sequence

TYPE_ERROR_MSG = "Unsupported input type: use either a list or a tuple"
VALUE_ERROR_MSG = "Unsupported input value: citations cannot be neither empty nor None"


def h_index(citations: Sequence[int]) -> int:
    """Return the highest number of papers h having at least h citations"""
    _error_handling(citations)
    for i in range(len(citations), 0, -1):
        passing_cit = 0
        for cit in citations:
            if i <= cit:
                passing_cit += 1
        if i <= passing_cit:
            return i
    return 0


def i10_index(citations: Sequence[int]) -> int:
    """Return the number of papers having at least 10 citations"""
    _error_handling(citations)
    return len([cit for cit in citations if 10 <= cit])


def _error_handling(citations: Sequence[int]) -> None:
    if citations is None:
        raise ValueError(VALUE_ERROR_MSG)

    if not (isinstance(citations, list) or isinstance(citations, tuple)):
        raise TypeError(TYPE_ERROR_MSG)

    if len(citations) == 0:
        raise ValueError(VALUE_ERROR_MSG)

    for cit in citations:
        if not isinstance(cit, int) or cit < 0:
            raise ValueError(VALUE_ERROR_MSG)


if __name__ == '__main__':
    print(h_index([0, 0, 1, 1, 10, 5, 11, 13])) #4
    print(h_index([0, 0, 1, 1, 10, 5, 1, 3])) #3
    print(h_index(list(range(0, 10))))  #5
    print(h_index((0, 0, 1, 1))) #1
    print(h_index((1000, 10, 9, 1, 10, 5, 1, 3))) #5
    print(h_index([0] * 5)) #0

    print()

    print(i10_index([0, 0, 1, 1, 10, 5, 11, 13]))  #3
    print(i10_index([0, 0, 1, 1, 10, 5, 1, 3]))  #1
    print(i10_index(list(range(0, 10))))  #0
    print(i10_index((0, 0, 1, 1)))  #0
    print(i10_index((1000, 10, 9, 1, 10, 5, 1, 3)))  #3
    print(i10_index([0] * 5))  #0