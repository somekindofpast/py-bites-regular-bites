import re

VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    return True if re.sub('[' + VOWELS + ']', '', input_str, flags=re.IGNORECASE) == '' else False


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    return False if re.findall('[' + PYTHON + ']', input_str, flags=re.IGNORECASE) == [] else True


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    return False if re.findall('[0-9]', input_str) == [] else True


if __name__ == '__main__':
    print(contains_only_vowels('AE123'))
    print(contains_any_py_chars('america'))
    print(contains_digits('am3rica'))