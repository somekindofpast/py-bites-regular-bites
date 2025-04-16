import os
import urllib.request
from collections import Counter

# PREWORK
TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

# start coding

def load_words() -> list[str]:
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY) as f:
        lines = f.read().splitlines()
    return lines


def calc_word_value(word: str) -> int:
    """Given a word calculate its value using the LETTER_SCORES dict"""
    value = 0
    for letter in word:
        letter = letter.upper()
        if letter not in LETTER_SCORES.keys():
            return 0
        value += LETTER_SCORES[letter]
    return value


def max_word_value(words: list[str]) -> str:
    """Given a list of words calculate the word with the maximum value and return it"""
    counter = Counter()
    for word in words:
        counter[word] = calc_word_value(word)
    return counter.most_common(1)[0][0]


if __name__ == '__main__':
    print(len(load_words()))
    print(calc_word_value("bob"))
    print(calc_word_value("JuliaN"))
    print(calc_word_value("PyBites"))
    print(calc_word_value("benzalphenylhydrazone"))
    print(max_word_value(load_words()[20000:21000]))
    print(max_word_value(["a", "åäö"]))