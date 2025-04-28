import argparse
import math


def calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    if not isinstance(operation, str) or not isinstance(numbers, list) or len(numbers) == 0:
        raise SystemExit

    res = None
    for num in numbers:
        num = float(num)
        if not res:
            res = num
            continue
        match operation:
            case "add":
                res += num
            case "sub":
                res -= num
            case "mul":
                res *= num
            case "div":
                res /= num
    res = round(res, 2)
    return math.trunc(res) if res == math.trunc(res) else res


def create_parser():
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    _parser = argparse.ArgumentParser(description="a simple calculator")
    group = _parser.add_mutually_exclusive_group()
    group.add_argument("--add", nargs='*')
    group.add_argument("--sub", nargs='*')
    group.add_argument("--mul", nargs='*')
    group.add_argument("--div", nargs='*')
    return _parser


def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == '__main__':
    __parser = create_parser()

    __args = __parser.parse_args(['--add'] + ['1', '2', '3'])
    print(call_calculator(__args)) # 6
    __args = __parser.parse_args(['--sub'] + ['11', '9', '2.2', '1.8'])
    print(call_calculator(__args)) # -2
    __args = __parser.parse_args(['--mul'] + ['3.5', '2', '4.2'])
    print(call_calculator(__args)) # 29.4
    __args = __parser.parse_args(['--div'] + ['3', '2', '3', '5'])
    print(call_calculator(__args)) # 0.1