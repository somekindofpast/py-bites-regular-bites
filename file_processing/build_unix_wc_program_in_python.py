import os
import urllib.request
from typing import Tuple
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
harry_file = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/driving.py',
    harry_file
)

def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    text = open(file_, "r", newline='')
    lines = text.read().splitlines()
    text.close()
    words = 0
    chars = 0
    for line in lines:
        words += len(line.split())
        chars += len(line)
    return ' '.join([str(len(lines)), str(words), str(chars)])


print(wc(harry_file))


