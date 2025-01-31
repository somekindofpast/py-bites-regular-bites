from collections import Counter


def is_anagram(word1: str, word2: str) -> bool:
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    if word1 == word2:
        return False
    counter_word1 = _get_letter_counter(word1)
    counter_word2 = _get_letter_counter(word2)
    if len(counter_word1.keys()) != len(counter_word2.keys()):
        return False
    return len({key: value for (key, value) in counter_word1.items() if counter_word1[key] != counter_word2[key]}) == 0


def _get_letter_counter(word: str) -> Counter:
    counter = Counter()
    for letter in word:
        if letter.isalpha() or letter.isdigit():
            counter[letter.lower()] += 1
    return counter


if __name__ == '__main__':
    print(is_anagram("forty five", "over fifty"))
    print(is_anagram("forty five", "over fifty1"))