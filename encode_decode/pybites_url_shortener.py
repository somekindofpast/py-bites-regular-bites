from collections import deque
from math import floor
from string import ascii_lowercase, ascii_uppercase, digits
from typing import Dict

CODEX: str = digits + ascii_lowercase + ascii_uppercase
BASE: int = len(CODEX)
# makeshift database record
LINKS: Dict[int, str] = {
    1: "https://pybit.es",
    45: "https://pybit.es/pages/articles.html",
    255: "http://pbreadinglist.herokuapp.com",
    600: "https://pybit.es/pages/challenges.html",
    874: "https://stackoverflow.com",
}
SITE: str = "https://pybit.es"

# error messages
INVALID = "Not a valid PyBites shortened url"
NO_RECORD = "Not a valid shortened url"


def encode(record: int) -> str:
    """Encodes an integer into Base62"""
    res = ""
    queue = deque([record])
    while 0 < len(queue):
        num = queue.popleft()
        quotient = floor(num / 62)
        remainder = num % 62
        res = CODEX[remainder] + res
        if 0 < quotient:
            queue.append(quotient)
    return res


def decode(short_url: str) -> int:
    """Decodes the Base62 string into a Base10 integer"""
    value = 0
    for char in short_url:
        value = 62 * value + CODEX.find(char)
    return value


def redirect(url: str) -> str:
    """Retrieves URL from shortened DB (LINKS)

    1. Check for valid domain
    2. Check if record exists
    3. Return URL stored in LINKS or proper message
    """
    url_parts = url.split(SITE + "/")
    if not url.startswith(SITE + "/") or len(url_parts) != 2:
        return INVALID

    try:
        base10_val = decode(url_parts[1])
    except:
        return NO_RECORD

    if base10_val not in LINKS.keys():
        return NO_RECORD

    return LINKS[base10_val]


def shorten_url(url: str, next_record: int) -> str:
    """Shortens URL and updates the LINKS DB

    1. Encode next_record
    2. Adds url to LINKS
    3. Return shortened URL
    """
    base62_str = encode(next_record)
    LINKS[next_record] = url
    return SITE + "/" + base62_str


if __name__ == "__main__":
    print(encode(244)) #3W
    print(encode(4576))  #1bO
    print(encode(324))  #5e
    print(encode(768))  #co
    print(encode(4357))  #18h
    print(encode(7584))  #1Yk
    print(encode(234))  #3M
    print(encode(286438245))  #jnRFH
    print(encode(5000))  #1iE
    print(encode(6000))  #1yM
    print(encode(7000))  #1OU
    print(encode(8000))  #252
    print(encode(9000))  #2la
    print(encode(9999))  #2Bh
    print(decode("1C")) # 100
    short_url = shorten_url("https://youtube.com", 6000)
    print(short_url) #https://pybit.es/1yM
    print(redirect(short_url)) #https://youtube.com