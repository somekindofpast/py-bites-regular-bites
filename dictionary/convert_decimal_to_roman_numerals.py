
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

roman_numerals = [
    dict(zip(digits, ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'])),
    dict(zip(digits, ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'])),
    dict(zip(digits, ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'])),
    dict(zip(digits, ['M', 'MM', 'MMM', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'])),
]

def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    if not isinstance(decimal_number, int) or not 0 < decimal_number < 4000:
        raise ValueError

    res = ""
    dec_str = str(decimal_number)
    for i in range(len(dec_str)):
        num = int(dec_str[-1 - i])
        if num != 0:
            res = f"{roman_numerals[i][num]}{res}"
    return res


if __name__ == '__main__':
    print(romanize(1599))