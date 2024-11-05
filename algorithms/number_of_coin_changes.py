from typing import List


def make_changes(n: int, coins: List[int]) -> int:
    """
    Input: n - the changes amount
          coins - the coin denominations
    Output: how many ways to make this changes
    """
    if n == 0:
        return 0

    last_index = len(coins) - 1
    if coins[last_index] == 1:
        return 1

    div = int(n / coins[last_index])
    mod = int(n % coins[last_index])
    result = 0
    result += make_changes(n, coins[:last_index])
    for i in range(div):
        next_n = n - ((i + 1) * coins[last_index])
        result += make_changes(next_n, coins[:last_index])

    if 0 < div and mod == 0:
        result += 1

    return result


if __name__ == '__main__':
    british = [1, 2, 5, 10, 20, 50]
    usa = [1, 5, 10, 25, 50]

    print(make_changes(20, british))