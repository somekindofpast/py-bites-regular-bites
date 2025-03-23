from typing import List, TypeVar
T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError
    results = []
    for num in numbers:
        num *= pow(10, n)
        results.append(int(str(num)[:(n+1 if num < 0 else n)]))
    return results


if __name__ == '__main__':
    n_digit_numbers([-1.1, 2.22, -3.333], 3)