from datetime import datetime, timedelta
import re

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)


def add_todo(delay_time: str, task: str,
             start_time: datetime = NOW) -> str:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """
    try:
        return f"{task} @ {start_time + timedelta(seconds=int(delay_time))}"
    except:
        pass

    sec_match   = re.search(r"\d+s", delay_time)
    min_match   = re.search(r"\d+m", delay_time)
    hour_match  = re.search(r"\d+h", delay_time)
    day_match   = re.search(r"\d+d", delay_time)

    seconds     = 0 if sec_match    is None else int(sec_match.group().rstrip('s'))
    minutes     = 0 if min_match    is None else int(min_match.group().rstrip('m'))
    hours       = 0 if hour_match   is None else int(hour_match.group().rstrip('h'))
    days        = 0 if day_match    is None else int(day_match.group().rstrip('d'))

    return f"{task} @ {start_time + timedelta(seconds=seconds, minutes=minutes, hours=hours, days=days)}"


if __name__ == '__main__':
    print(add_todo("11h 10m", "Wash my car"))
    print(add_todo("30d", "Code a Bite"))
    print(add_todo("5m 3s", "Go to Bed"))
    print(add_todo("45", "Finish this Test"))
    print(add_todo("1d 10h 47m 17s", "Study some Python"))
