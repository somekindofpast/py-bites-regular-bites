def validate_pangram(sentence: str) -> bool:
    """Check if a sentence is a pangram
    A pangram is a sentence containing every letter in the English alphabet.
    The input `sentence` should be a string containing only English letters.
    The function returns True if the sentence is a pangram, and False otherwise.
    """
    letters = ''.join(sentence.lower().split())
    result_set = set()
    for letter in letters:
        result_set.add(letter)
    return len(result_set) == 26


if __name__ == "__main__":
    print(validate_pangram("The quick brown fox jumps over a lazy dog"))
    print(validate_pangram("thequickbrownfoxjumpsoverthelazydog"))
    print(validate_pangram("PYBITES IS A COMMUNITY OF PYTHON CODERS"))