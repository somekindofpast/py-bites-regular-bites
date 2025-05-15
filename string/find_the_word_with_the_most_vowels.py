from collections import Counter

VOWELS = list('aeiou')


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    counter = Counter()
    for word in str(text).split():
        counter[word.lower()] = len([c for c in word.lower() if c in VOWELS])
    return counter.most_common(1)[0]