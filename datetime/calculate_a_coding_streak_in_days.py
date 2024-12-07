import re
from datetime import datetime, timedelta, date

TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    date_strings: set[str] = set(re.findall(r"\d\d\d\d-\d\d-\d\d", data))
    return [date(int(date_string.split('-')[0]), int(date_string.split('-')[1]), int(date_string.split('-')[2])) for date_string in date_strings]


def calculate_streak(dates) -> int:
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    delta = timedelta(days=1)
    for activity_date in sorted(dates, reverse=True):
        if isinstance(activity_date, date) and (TODAY - activity_date).days <= delta.days:
            delta = timedelta(days=delta.days + 1)
        else:
            break
    return delta.days - 1


if __name__ == '__main__':
    data_ = """
        +------------+------------+---------+
        | date       | activity   | count   |
        |------------+------------+---------|
        | 2018-11-12 | pcc        | 1       |
        | 2018-11-11 | 100d       | 1       |
        | 2018-11-10 | 100d       | 2       |
        | 2018-10-15 | pcc        | 1       |
        | 2018-10-15 | pcc        | 1       |
        | 2018-10-05 | bite       | 1       |
        | 2018-09-21 | bite       | 4       |
        | 2018-09-18 | bite       | 2       |
        | 2018-09-16 | bite       | 4       |
        +------------+------------+---------+
        """
    print(calculate_streak(extract_dates(data_)))