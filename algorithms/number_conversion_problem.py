current: str = ""

def dec_to_base(number, base) -> int:
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    recur(number, base, 0)
    global current
    result = current
    current = ""
    return int(result)

def recur(number, base, power) -> int:
    res: int = int(number / (base ** power))
    if 0 < res:
        remainder: int = recur(number, base, power + 1)
        division: int = int(remainder / (base ** power))
        global current
        current += str(division)[-1]
        return int(remainder % (base ** power))
    else:
        return int(number % (base ** power))


if __name__ == '__main__':
    print(dec_to_base(7, 2))