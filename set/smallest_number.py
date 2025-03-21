from typing import List


def minimum_number(digits: List[int]) -> int:
    if digits is None or len(digits) == 0:
        return 0
    num_str = ""
    for digit in sorted(set(digits)):
        num_str += str(digit)
    return int(num_str)