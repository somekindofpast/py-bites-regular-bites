import os
import urllib.request
from typing import Tuple
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_file = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_file
)


def get_harry_most_common_word() -> Tuple[int, int]:
    harry_text = open(harry_file, "r")
    stopwords_text = open(stopwords_file, "r")
    lines = harry_text.read().splitlines()
    stopwords = stopwords_text.read().splitlines()
    counter = Counter()

    for line in lines:
        if line == '':
            continue
        line = ''.join(char for char in line.lower().strip() if char.isalnum() or char == ' ')
        words = line.split()
        for word in words:
            if word not in stopwords:
                counter[word] += 1

    harry_text.close()
    stopwords_text.close()

    return counter.most_common(1)[0]


if __name__ == '__main__':
    print(get_harry_most_common_word())