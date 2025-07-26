import calendar
from datetime import date, timedelta


ERROR_MSG = (
    "Unambiguous value passed, please specify either start_month or show_workdays"
)
FEDERAL_HOLIDAYS = (
    date(2020, 9, 7),
    date(2020, 10, 12),
    date(2020, 11, 11),
    date(2020, 11, 26),
    date(2020, 12, 25),
)
WFH = (calendar.TUESDAY, calendar.WEDNESDAY)
WEEKENDS = (calendar.SATURDAY, calendar.SUNDAY)
AT_HOME = WFH + WEEKENDS

def four_day_weekends(*args,
        start_month: int = 8,
        paid_time_off: int = 200,
        year: int = 2020,
        show_workdays: bool = False
    ) -> None:
    """Generates four day weekend report

    The four day weekends are calculated from the start_month through the end of the year
    along with the number of work days for the same time period. The reports takes into
    account any holidays that might fall within that time period and days designated as
    working from home (WFH).

    If show_workdays is set to True, a report with the work days is generated instead of
    the four day weekend dates.

    Args:
        start_month (int, optional): Month to start. Defaults to 8.
        paid_time_off (int, optional): Paid vacation days
        year (int, optional): Year to calculate, defaults to current year
        show_workdays (bool, optional): Enables work day report. Defaults to False.

    Raises:
        ValueError: ERROR_MSG
    """
    if 0 < len(args):
        raise ValueError(ERROR_MSG)

    text_calendar = calendar.TextCalendar()
    if not show_workdays:

        holidays = list(FEDERAL_HOLIDAYS)
        weekend_periods = []
        all_days = []
        for month in range(start_month, 12 + 1):
            for week in text_calendar.monthdatescalendar(year, month):
                all_days.extend(week)

        for d in all_days:
            if start_month <= d.month and calendar.weekday(d.year, d.month, d.day) == calendar.FRIDAY and (d + timedelta(days=3)) in all_days:
                weekend_periods.append((d, d + timedelta(days=3)))

        weekend_periods = sorted(set(weekend_periods))
        for i in range(len(weekend_periods)-1, -1, -1):
            holiday_week = False
            for holiday in holidays:
                if holiday.month == weekend_periods[i][0].month and weekend_periods[i][0] <= holiday <= weekend_periods[i][1]:
                    holidays.remove(holiday)
                    holiday_week = True
                    break
            if holiday_week:
                weekend_periods.pop(i)

        pto_days = int(paid_time_off / 8)
        num_weekends = len(weekend_periods)
        balance = pto_days - num_weekends * 2
        print(f"{num_weekends} Four-Day Weekends")
        print("========================")
        print(f"PTO: {paid_time_off} ({pto_days} days)")
        print(f"BALANCE: {balance * 8} ({abs(balance)} days)")
        print()
        for i in range(num_weekends):
            period = weekend_periods[i]
            print(f"{period[0]} - {period[1]}{' *' if balance < 0 and ((i+1)*2 == abs(balance)+1 or (i+1)*2 == abs(balance)+2) else ''}")
    else:
        weekdays = []
        weekend_periods = []
        all_days = []
        for month in range(start_month, 12 + 1):
            for week in text_calendar.monthdatescalendar(year, month):
                all_days.extend(week)

        for d in all_days:
            if start_month <= d.month and calendar.weekday(d.year, d.month, d.day) == calendar.FRIDAY and (d + timedelta(days=3)) in all_days:
                period = [d, d + timedelta(days=1), d + timedelta(days=2), d + timedelta(days=3)]
                holiday_week = False
                for to_add in period:
                    if to_add in FEDERAL_HOLIDAYS:
                        holiday_week = True
                        break
                if not holiday_week:
                    weekend_periods.extend(period)

        for d in all_days:
            if start_month <= d.month and calendar.weekday(d.year, d.month, d.day) not in AT_HOME and d not in FEDERAL_HOLIDAYS and d not in weekend_periods:
                weekdays.append(d)

        weekdays = sorted(set(weekdays))
        print(f"Remaining Work Days: {len(weekdays) * 8} ({len(weekdays)} days)")
        for d in weekdays:
            print(d)


if __name__ == "__main__":
    four_day_weekends()
    print()
    four_day_weekends(show_workdays=True)
    print()
    four_day_weekends(start_month=10)
    print()
    four_day_weekends(start_month=10, show_workdays=True)
    print()
    four_day_weekends(start_month=10, paid_time_off=120)
    print()
    four_day_weekends(start_month=10, paid_time_off=284)
    print()
    four_day_weekends(paid_time_off=160)