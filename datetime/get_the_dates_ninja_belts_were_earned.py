import json
import os
from collections import OrderedDict
from pathlib import Path

from dateutil.parser import parse

SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
BELTS = ('white yellow orange green blue brown black '
         'paneled red').split()
TMP = Path(os.getenv("TMP", "/tmp"))


def get_belts(file_path: Path) -> dict:
    """Parsed the passed in json data:
       {"date":"5/1/2019","score":1},
       {"date":"9/13/2018","score":3},
       {"date":"10/25/2019","score":1},

       Loop through the scores in chronological order,
       determining when belts were achieved (use SCORES
       and BELTS).

       Return a dict with keys = belts, and values =
       readable dates, example entry:
       'yellow': 'January 25, 2018'
    """
    if file_path.exists():
        score_dates = json.loads(file_path.read_text())
    else:
        return {}

    score_dates = sorted(score_dates, key=lambda x: parse(x['date'], dayfirst=False))
    score = 0
    belt_index = 0
    res: dict[str, str] = OrderedDict()
    for score_date in score_dates:
        score += score_date['score']
        if SCORES[belt_index] <= score:
            date = parse(score_date['date'], dayfirst=False)
            res[BELTS[belt_index]] = date.strftime("%B %d, %Y")

            belt_index += 1
            if len(SCORES) <= belt_index:
                break
    return res


if __name__ == "__main__":
    from urllib.request import urlretrieve

    file_name = f'bite_scores1.json'
    file_path_ = TMP / file_name
    remote = 'https://bites-data.s3.us-east-2.amazonaws.com/'
    if not file_path_.exists():
        urlretrieve(f'{remote}{file_name}',
                    file_path_)

    print(get_belts(file_path_))