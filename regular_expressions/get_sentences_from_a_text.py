import re

def get_sentences(text):
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""
    text = ' '.join([line.strip() for line in text.splitlines()]).strip()
    return re.findall(r"([A-Z].*?[.?!])(?=\s[A-Z]|$)", text)


if __name__ == "__main__":
    TEXT = """
    PyBites was founded 19th of December 2016. That means that today,
    14th of October 2019 we are 1029 days old. Time flies when you code
    in Python. Anyways, good luck with this Bite. What is your favorite editor?
    """
    print(get_sentences(TEXT))

    TEXT_WITH_DOTS = """
    We are looking forward attending the next Pycon in the U.S.A.
    in 2020. Hope you do so too. There is no better Python networking
    event than Pycon. Meet awesome people and get inspired. Btw this
    dot (.) should not end this sentence, the next one should. Have fun!
    """
    print(get_sentences(TEXT_WITH_DOTS))