import string
from collections import Counter

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password) -> bool:
    if not isinstance(password, str) or not (6 <= len(password) <= 12) or password in used_passwords:
        return False

    counter = Counter()
    for c in password:
        if c.isdigit():
            counter["digit"] += 1
        elif c in string.ascii_lowercase:
            counter["lower"] += 1
        elif c in string.ascii_uppercase:
            counter["upper"] += 1
        elif c in PUNCTUATION_CHARS:
            counter["punctuation"] += 1

    if not (1 <= counter["digit"] and 2 <= counter["lower"] and 1 <= counter["upper"] and 1 <= counter["punctuation"]):
        return False

    used_passwords.add(password)
    return True