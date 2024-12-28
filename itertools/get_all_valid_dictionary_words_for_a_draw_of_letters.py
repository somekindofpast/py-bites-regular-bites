import itertools
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    possible_words = []
    for letters in _get_permutations_draw(draw):
        word = "".join(letters).lower()
        if word in dictionary:
            possible_words.append(word)
    return possible_words

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    result = []
    [result.extend(itertools.permutations(draw, n)) for n in range(2, len(draw) + 1)]
    return result


if __name__ == '__main__':
    draw_ = "T, I, I, G, T, T, L".split(", ")
    #[print(item) for item in _get_permutations_draw(draw_)]
    print(get_possible_dict_words(draw_))