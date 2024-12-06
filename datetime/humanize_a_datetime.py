from collections import namedtuple
from datetime import datetime, timedelta

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if not isinstance(date, datetime):
        raise ValueError("Given argument is not a date")
    if NOW < date:
        raise ValueError("Given date is in the future")

    time_delta = NOW - date
    delta_seconds = time_delta.days * DAY + time_delta.seconds

    for time_offset in TIME_OFFSETS:
        if delta_seconds < time_offset.offset:
            return str(time_offset.date_str).format(delta_seconds if not time_offset.divider else int(delta_seconds / time_offset.divider))

    return f"{date.month:0>2}/{date.day:0>2}/{date.year % 1000}"


if __name__ == "__main__":
    print(pretty_date(NOW - timedelta(seconds=5)))
    print(pretty_date(NOW - timedelta(seconds=15)))
    print(pretty_date(NOW - timedelta(seconds=90)))
    print(pretty_date(NOW - timedelta(minutes=59)))
    print(pretty_date(NOW - timedelta(minutes=60)))
    print(pretty_date(NOW - timedelta(hours=1)))
    print(pretty_date(NOW - timedelta(hours=2)))
    print(pretty_date(NOW - timedelta(days=1, hours=23)))
    print(pretty_date(datetime(2024, 12, 4, 10, 10, 43, 621833)))