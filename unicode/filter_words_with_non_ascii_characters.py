import re
from string import ascii_lowercase, ascii_uppercase


def extract_non_ascii_words(text: str) -> list[str]:
    """Filter a text returning a list of non-ascii words"""
    text = re.sub(r"[?!,.;:/\\-]", '', text)
    res = []
    for word in text.split():
        for c in word:
            if c not in ascii_lowercase + ascii_uppercase + '0123456789':
                res.append(word)
                break
    return res


if __name__ == '__main__':
    print(extract_non_ascii_words("extrAct the0se: -?!,.;/\\ \u0e55\u0e57 but not these"))