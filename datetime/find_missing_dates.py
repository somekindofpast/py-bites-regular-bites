from datetime import timedelta, date
from typing import List


def get_missing_dates(dates: List[date]) -> List[date]:
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    dates = sorted(dates)
    missing_dates: List[date] = []
    cur_date = dates[0]
    while cur_date < dates[-1]:
        if cur_date not in dates:
            missing_dates.append(cur_date)
        cur_date = cur_date + timedelta(days=1)
    return missing_dates


if __name__ == '__main__':
    date_range = [
        date(2019, 2, 1),
        date(2019, 2, 3),
        date(2019, 2, 5),
        date(2019, 2, 7),
        date(2019, 2, 9),
    ]
    print(get_missing_dates(date_range))