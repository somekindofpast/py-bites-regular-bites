from collections import deque
from string import ascii_letters


def reverse_letters(string: str) -> str:
    """Reverse letters in a string but keep the order of the non-letters the same"""
    queue = deque([c for c in string if c in ascii_letters])
    result = ""
    for c in string:
        if c in ascii_letters:
            result += queue.pop()
        else:
            result += c
    return result


if __name__ == "__main__":
    print(reverse_letters("ab-cd"))
    print(reverse_letters("ab5DEf"))
    print(reverse_letters("a-bC-dEf-ghIj"))