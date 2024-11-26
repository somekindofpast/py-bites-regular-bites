import os
from collections import Counter
from pathlib import Path
from urllib.request import urlretrieve
from csv import DictReader

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
TMP = Path(os.getenv("TMP", "/tmp"))
stats = TMP / 'bites.csv'

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """

    with open(stats, newline='', encoding='utf-8-sig') as csvfile:
        rows = list(DictReader(csvfile, delimiter=';'))

    counter = Counter()
    for row in rows:
        if row["Difficulty"] != "None":
            counter[row["Bite"]] = row["Difficulty"]

    return [tup[0].split()[1].strip('.') for tup in counter.most_common(N)]


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)