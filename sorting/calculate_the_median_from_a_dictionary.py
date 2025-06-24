def calc_median_from_dict(d: dict) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """
    magnitude_list = []
    for count in d.values():
        if not isinstance(count, int):
            raise TypeError
        magnitude_list.append(count / 10 if count % 10 == 0 else 0)
    magnitude = int(sorted(magnitude_list)[0])

    num_list = []
    for num, count in d.items():
        count = count / magnitude if magnitude != 0 else count
        num_list.extend([num] * count)
    num_list.sort()
    length = len(num_list)
    mid = int(length / 2)
    res = float(num_list[mid]) if length % 2 == 1 else float(num_list[mid-1] + num_list[mid]) / 2.0
    return res * magnitude if magnitude != 0 else res