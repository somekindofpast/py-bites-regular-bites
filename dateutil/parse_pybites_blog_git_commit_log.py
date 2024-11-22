from collections import Counter
import os
from typing import Tuple
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(
    commit_log: str = commits,
    year: int = None
) -> Tuple[str, str]:
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    with open(commit_log) as f:
        logs = f.readlines()
    counter = Counter()
    for log in logs:
        log = log.lstrip("Date:").strip()
        date_mods = log.split(" | ")
        datetime_obj = parse(date_mods[0])
        if year and year != datetime_obj.year:
            continue
        insertions = 0
        deletions = 0
        for mod in date_mods[1].split(", "):
            if "insertions" in mod:
                insertions = int(mod.split()[0])
            elif "deletions" in mod:
                deletions = int(mod.split()[0])
        counter[f"{datetime_obj.year}-{datetime_obj.month:02d}"] += insertions + deletions
    return counter.most_common()[-1][0], counter.most_common()[0][0]


if __name__ == '__main__':
    print(get_min_max_amount_of_commits(year=None))
    print(get_min_max_amount_of_commits(year=2017))
    print(get_min_max_amount_of_commits(year=2018))
    print(get_min_max_amount_of_commits(year=2019))