from collections import Counter


def major_n_minor(numbers: list[int]):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    counter = Counter()
    for num in numbers:
        counter[num] += 1
    return counter.most_common()[0][0], counter.most_common()[-1][0]