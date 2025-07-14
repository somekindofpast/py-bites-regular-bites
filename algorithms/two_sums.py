def two_sums(numbers, target):
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    res = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] + numbers[j] == target:
                res.append((i, j))

    return sorted(res, key=lambda tup: numbers[tup[0]])[0] if 0 < len(res) else None


if __name__ == "__main__":
    NUMBERS = [
        2202, 9326, 1034, 4180, 1932, 8118, 7365, 7738, 6220, 3440, 1538, 7994, 465,
        6387, 7091, 9953, 35, 7298, 4364, 3749, 9686, 1675, 5201, 502, 366, 417,
        8871, 151, 6246, 3549, 6916, 476, 8645, 3633, 7175, 8124, 9059, 3819, 5664,
        3783, 3585, 7531, 4748, 353, 6819, 9117, 1639, 3046, 4857, 1981]
    print(two_sums(NUMBERS, 5224))