from functools import wraps


def int_args(func):
    @wraps(func)
    # complete this decorator
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError
            if arg < 0:
                raise ValueError
        return func(*args)
    return wrapper


if __name__ == '__main__':
    @int_args
    def sum_numbers(*numbers):
        return sum(numbers)


    print(sum_numbers(1, 2, 3))