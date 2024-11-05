from typing import List


def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    if N < 1:
        return []
    triangle: List[List[int]] = []
    for row in range(N):
        if row == 0:
            triangle = [[0, 1, 0]]
            continue

        triangle.append([0])
        for col in range(len(triangle[row - 1]) - 1):
            triangle[row].append(triangle[row - 1][col] + triangle[row - 1][col + 1])
        triangle[row].append(0)

    return triangle[N - 1][1:-1]


if __name__ == '__main__':
    print(f"Result: {pascal(5)}")