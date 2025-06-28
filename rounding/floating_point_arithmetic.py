from typing import Generator

VALUES = "[0.1, 0.2, 0.3, 0.005, 0.005, 2.67]"


def calc_sums(values: str = VALUES) -> Generator[str, None, None]:
    """
    Process the above JSON-encoded string of values and calculate the sum of each adjacent pair.

    The output should be a generator that produces a string that recites the calculation for each pair, for example:

        'The sum of 0.1 and 0.2, rounded to two decimal places, is 0.3.'
    """
    values = values.strip('[]').split(", ")
    for i in range(1, len(values)):
        n1 = float(values[i-1])
        n2 = float(values[i])
        sum_ = n1 + n2
        if 2 < len(str(sum_).split('.')[1]) and str(sum_)[-1] == '5':
            sum_ = float(str(sum_)[:-1] + '6')
        yield f"The sum of {n1} and {n2}, rounded to two decimal places, is {'%.2f' % round(sum_, 2)}."


if __name__ == "__main__":
    print(list(calc_sums()))