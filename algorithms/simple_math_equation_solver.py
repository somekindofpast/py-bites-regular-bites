from itertools import permutations
from operator import add, sub, mul
from typing import List, Union, Iterable

def find_all_solutions(operator_path: List[str], expected_result: int) -> Union[List[List[int]], Iterable[List[int]]]:
    # blank canvas to fill

    for op in operator_path:
        if op not in ['+', '-', '*']:
            raise ValueError("non-supported operator {}".format(op))

    if isinstance(expected_result, float):
        raise ValueError("result of type float")

    solutions = []
    for permut in permutations(range(1, 10), len(operator_path) + 1):
        permut_list = [permut[0]]
        operator_list = []
        for i in range(len(operator_path)):
            if operator_path[i] == '*':
                permut_list[-1] = permut_list[-1] * permut[i + 1]
            else:
                operator_list.append(operator_path[i])
                permut_list.append(permut[i + 1])

        result = permut_list[0]
        for i in range(len(operator_list)):
            next_num = permut_list[i + 1]
            if operator_list[i] == '+':
                result += next_num
            elif operator_list[i] == '-':
                result -= next_num
        if result == expected_result:
            solutions.append(list(permut))

    return solutions


if __name__ == '__main__':
    print(find_all_solutions(["+", "*", "*", "+", "*", "-"], 528))
