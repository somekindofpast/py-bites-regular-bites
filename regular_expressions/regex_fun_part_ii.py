import re


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    return re.match(r'.*(\d\d\d\d)-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d).*', text) is not None


def is_integer(number):
    """Return True if number is an integer"""
    return isinstance(number, int)


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    return re.match(r'.*\w-\w.*', text) is not None


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    return re.sub(r'\s+\(.*?\)', '', text)


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    return [string.strip() for string in re.split(r'[?!.,;]', text) if string != '']


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    return re.sub(r'\s+', ' ', text)


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    return re.match(r'.*[aeiouAEIOU]{3}.*', word) is not None


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    return re.sub(r'(\d\d)/(\d\d)/(\d\d\d\d)', r'\2/\1/\3', date)


if __name__ == '__main__':
    print('has_timestamp:', has_timestamp('INFO 2014-07-03T23:27:51 Shutdown initiated.'))
    print('has_timestamp:', has_timestamp('INFO 2014-06-01T13:28:51 Shutdown initiated.'))
    print('has_timestamp:', has_timestamp('INFO 2014-7-3T23:27:51 Shutdown initiated.'))
    print('has_timestamp:', has_timestamp('INFO 2014-07-03t23:27:1 Shutdown initiated.'))

    print('is_integer:', is_integer(1))
    print('is_integer:', is_integer(-1))
    print('is_integer:', is_integer('str'))
    print('is_integer:', is_integer(1.1))

    print('has_word_with_dashes:', has_word_with_dashes('this Bite is self-contained'))
    print('has_word_with_dashes:', has_word_with_dashes('the match ended in 1-1'))
    print('has_word_with_dashes:', has_word_with_dashes('this Bite is not selfcontained'))
    print('has_word_with_dashes:', has_word_with_dashes('the match ended in 1- 1'))

    print('remove_all_parenthesis_words:', remove_all_parenthesis_words('good morning (afternoon), how are you?'))
    print('remove_all_parenthesis_words:', remove_all_parenthesis_words('math (8.6) and science (9.1) where his strengths'))

    print('split_string_on_punctuation:', split_string_on_punctuation('hi, how are you doing? blabla'))
    print('split_string_on_punctuation:', split_string_on_punctuation(';String. with. punctuation characters!'))

    print('remove_duplicate_spacing:', remove_duplicate_spacing('This is a   string with  too    much spacin'))

    print('has_three_consecutive_vowels:', has_three_consecutive_vowels('beautiful'))
    print('has_three_consecutive_vowels:', has_three_consecutive_vowels('queueing'))
    print('has_three_consecutive_vowels:', has_three_consecutive_vowels('mountain'))
    print('has_three_consecutive_vowels:', has_three_consecutive_vowels('house'))

    print('convert_emea_date_to_amer_date:', convert_emea_date_to_amer_date('31/03/2018'))
    print('convert_emea_date_to_amer_date:', convert_emea_date_to_amer_date('none'))