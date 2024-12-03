import collections
from datetime import datetime
import os
import re
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
RSS_FEED = 'pybites_feed.rss.xml'
PUB_DATE = re.compile(r'<pubDate>(.*?)</pubDate>')
TMP = os.getenv("TMP", "/tmp")

month_to_num = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}


def _get_dates():
    """Downloads PyBites feed and parses out all pub dates returning
       a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
       'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
    remote = os.path.join(BASE_URL, RSS_FEED)
    local = os.path.join(TMP, RSS_FEED)
    urlretrieve(remote, local)

    with open(local) as f:
        return PUB_DATE.findall(f.read())


def convert_to_datetime(date_str: str) -> datetime:
    """Receives a date str and convert it into a datetime object"""
    date_parts = date_str.split()
    time_parts = date_parts[4].split(':')
    return datetime(int(date_parts[3]), month_to_num[date_parts[2]], int(date_parts[1]), int(time_parts[0]), int(time_parts[1]))


def get_month_most_posts(dates: list[datetime]) -> str:
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most"""
    counter = collections.Counter()
    for date in dates:
        counter[f"{date.year}-{date.month}"] += 1
    month_str: str = counter.most_common(1)[0][0]
    return month_str if len(month_str) == 7 else f"{month_str.split('-')[0]}-0{month_str.split('-')[1]}"


if __name__ == "__main__":
    converted_dates = [convert_to_datetime(d) for d in _get_dates()]
    print(get_month_most_posts(converted_dates))