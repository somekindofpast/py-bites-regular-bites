from string import ascii_uppercase


def convert(number: int, base: int = 2) -> str:
    """Converts an integer into any base between 2 and 36 inclusive

    Args:
        number (int): Integer to convert
        base (int, optional): The base to convert the integer to. Defaults to 2.

    Raises:
        Exception (ValueError): If base is less than 2 or greater than 36
        TypeError: If number is not an integer

    Returns:
        str: The returned value as a string
    """
    if not isinstance(number, int) or not isinstance(base, int):
        raise TypeError
    if not (2 <= base <= 36):
        raise ValueError

    res = ""
    table = [num for num in range(10)] + [letter for letter in ascii_uppercase]
    while number != 0:
        res = f"{table[number % base]}{res}"
        number = int(number / base)
    return res