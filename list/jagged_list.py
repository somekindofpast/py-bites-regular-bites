from typing import List


def jagged_list(lst_of_lst: List[List[int]], fillvalue: int = 0) -> List[List[int]]:
    if not lst_of_lst:
        return []
    size = len(max(lst_of_lst, key=lambda x: len(x)))
    for lst in lst_of_lst:
        if len(lst) < size:
            lst.extend([fillvalue for _ in range(size - len(lst))])
    return lst_of_lst