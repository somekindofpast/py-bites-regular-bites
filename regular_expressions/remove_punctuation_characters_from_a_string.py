import re

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return re.sub('[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', '', input_string)


if __name__ == '__main__':
    print(remove_punctuation(';String. with. punctuation characters!'))