from difflib import SequenceMatcher
import os
from typing import Union
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, 'dictionary.txt')
if not os.path.isfile(DICTIONARY):
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/dictionary.txt',
        DICTIONARY
    )


def load_words():
    'return dict of words in DICTIONARY'
    with open(DICTIONARY) as f:
        return {word.strip().lower() for word in f.readlines()}


def suggest_word(misspelled_word: str, words: Union[set, None]) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    if words is None:
        words = load_words()

    ratio = 0.0
    res = ""
    for word in words:
        match_obj = SequenceMatcher(None, misspelled_word, word)
        if ratio < match_obj.ratio():
            ratio = match_obj.ratio()
            res = word

    return res


if __name__ == '__main__':
    words = load_words()
    print(suggest_word("acheive", words))
    print(suggest_word("acceptible", words))
    print(suggest_word("aquire", words))
    print(suggest_word("accomodate", words))