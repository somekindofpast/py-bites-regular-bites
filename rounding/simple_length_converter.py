def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if not isinstance(value, float) and not isinstance(value, int):
        raise TypeError
    fmt = fmt.lower()
    value = float(value)
    if fmt != "cm" and fmt != "in":
        raise ValueError

    CM_IN = 0.393700787
    IN_CM = 2.54

    if fmt == "in":
        return round(value * CM_IN, 4)
    else:
        return round(value * IN_CM, 4)