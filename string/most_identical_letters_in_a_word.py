import string
from collections import Counter
from typing import Tuple


def max_letter_word(text: str) -> Tuple[str, str, int]:
    """
    Find the word in text with the most repeated letters. If more than one word
    has the highest number of repeated letters choose the first one. Return a
    tuple of the word, the (first) repeated letter and the count of that letter
    in the word.
    #>>> max_letter_word('I have just returned from a visit...')
    ('returned', 'r', 2)
    #>>> max_letter_word('$5000 !!')
    ('', '', 0)
    """
    if not isinstance(text, str):
        raise ValueError
    result = None
    top_repetition = 0
    for word in text.split():
        word_original = word.strip(string.punctuation + string.digits + r'«¿»')
        word = word_original.casefold()
        if word == '':
            continue

        counter = Counter()
        for letter in word:
            if not letter.isalpha():
                continue
            counter[letter] += 1

        repetition = 0
        letter_most_repeat = ''
        for letter in word:
            if repetition < counter[letter]:
                repetition = counter[letter]
                letter_most_repeat = letter

        if letter_most_repeat != '' and top_repetition < repetition:
            top_repetition = repetition
            result = word_original, letter_most_repeat, repetition

    return ('', '', 0) if result is None else result


if __name__ == '__main__':
    print(max_letter_word('''It is a truth universally acknowledged, that a single man in
                    possession of a good fortune, must be in want of a wife.'''))
    print(max_letter_word('''20,000 Leagues Under the Sea is a 1954 American 
                    Technicolor science fiction-adventure film...'''))
    print(max_letter_word('emoji like 😃😃😃😃 are not letters'))
    print(max_letter_word('Société Générale est une des principales banques françaises'))
    print(max_letter_word('Short Plays By Lady Gregory The Knickerbocker Press 1916'))
    print(max_letter_word('six-feet-two in height'))
    print(max_letter_word('der Schloß is riesig'))
    print(max_letter_word('the quick brown fox jumped over the lazy dog'))
    print(max_letter_word('«¿Tiene sentido la TV pública?»'))
    print(max_letter_word("but we've been there already!!!"))
    print(max_letter_word('"____".isalpha() is True, thus this test text'))
    print(max_letter_word('99abc99 __abc__ --abc-- digits _ and - are not letters'))
    print(max_letter_word('test test test test test correct-answer.'))
    print(max_letter_word('They shouted "Oh no she didn\'t"'))
    print(max_letter_word("The brothers' feet were muddy."))
    print(max_letter_word('1, 2, 3'))
    print(max_letter_word(''))