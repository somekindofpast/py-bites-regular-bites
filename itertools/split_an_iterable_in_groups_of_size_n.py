import types
from itertools import islice


def group(iterable, n):
    """Splits an iterable set into groups of size n and a group
       of the remaining elements if needed.

       Args:
         iterable (list): The list whose elements are to be split into
                          groups of size n.
         n (int): The number of elements per group.

       Returns:
         list: The list of groups of size n,
               where each group is a list of n elements.
    """
    iter_list = list(iterable)
    res = [[]]
    for num in islice(iter_list, len(iter_list)):
        if len(res[-1]) == n:
            res.append([])
        res[-1].append(num)
    return res


if __name__ == '__main__':
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 3
    gen = (i for i in iterable)
    ret = group(gen, n)
    print(ret)