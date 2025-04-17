def positive_divide(numerator, denominator):
    if not (isinstance(numerator, int) or isinstance(numerator, float)):
        raise TypeError
    if not (isinstance(denominator, int) or isinstance(denominator, float)):
        raise TypeError
    if numerator < 0 < denominator or denominator < 0 < numerator:
        raise ValueError

    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return 0
    return result