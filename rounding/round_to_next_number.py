def round_to_next(number: int, multiple: int):
    if abs(number) == abs(multiple):
        return int(number / multiple) * multiple

    if number < 0 or multiple < 0:
        if number < 0 < multiple:
            return 0
        else:
            return int(number / multiple) * multiple + int(multiple if 0 < abs(number) % abs(multiple) else 0)
    else:
        return int(number / multiple) * multiple + int(multiple if 0 < number % multiple else 0)