char_dict = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

def generate_letter_combinations(digits: str) -> list[str]:
    """
    Calculate all possible letter combinations of a very short phone number.
    Input: A string of up to four digits.
    Output: A list of strings where each string represents a valid combination of letters
        that can be formed from the input. The strings in the output list should be sorted
        in lexicographical order.
    Raises: `ValueError`: If the input `digits` string contains non-digit characters or
        has more than four digits.
    """
    if not digits.isnumeric() or '0' in digits or '1' in digits or 4 < len(digits):
        raise ValueError("invalid input")

    results: list[str] = []
    for digit in digits:
        chars: list[str] = char_dict[digit]
        if not results:
            results += chars
        else:
            current = tuple(results)
            results.clear()
            results = [string + char for char in chars for string in current]
    return sorted(results)


if __name__ == "__main__":
    print(generate_letter_combinations("23"))
    print(generate_letter_combinations("79"))
    print(generate_letter_combinations("234"))
    print(generate_letter_combinations("222"))