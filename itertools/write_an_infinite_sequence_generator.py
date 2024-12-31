import itertools
import string


def sequence_generator():
    buffer = []
    [buffer.extend([ord(char) - ord('A') + 1, char]) for char in string.ascii_uppercase]
    return itertools.cycle(buffer)


if __name__ == '__main__':
    print(list(itertools.islice(sequence_generator(), 10)))
    print(list(itertools.islice(sequence_generator(), 52, 62)))
    print(list(itertools.islice(sequence_generator(), 146, 156)))