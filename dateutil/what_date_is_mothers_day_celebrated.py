from datetime import date

from dateutil.rrule import rrule, WEEKLY, SU


def get_mothers_day_date(year: int) -> date:
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    start_date = date(year, 5, 1)
    return [date_time.date() for date_time in list(rrule(freq=WEEKLY, dtstart=start_date, byweekday=SU, count=2))][1]


if __name__ == '__main__':
    print(get_mothers_day_date(2014))
    print(get_mothers_day_date(2017))
    print(get_mothers_day_date(2021))
    print(get_mothers_day_date(2024))