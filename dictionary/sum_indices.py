from collections import defaultdict
from typing import List


def sum_indices(items: List[str]) -> int:
    res = 0
    item_dict = defaultdict(list)
    for i in range(len(items)):
        indices = item_dict[items[i]]
        indices.append(i)
        res += sum(indices)
    return res