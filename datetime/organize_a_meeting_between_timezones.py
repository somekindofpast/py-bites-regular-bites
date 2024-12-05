from datetime import datetime
from zoneinfo import ZoneInfo, available_timezones

MIN_MEETING_HOUR = 6
MAX_MEETING_HOUR = 22
TIMEZONES = set(available_timezones())


def within_schedule(utc: datetime, *timezones):
    """
    Receive a UTC datetime and one or more timezones and check if
    they are all within MIN_MEETING_HOUR and MAX_MEETING_HOUR
    (both included).
    """
    utc = utc.replace(tzinfo=ZoneInfo("UTC"))
    for timezone in timezones:
        if timezone not in TIMEZONES:
            raise ValueError(f"Timezone unrecognized: {timezone}")
        hour = utc.astimezone(ZoneInfo(timezone)).hour
        if hour < MIN_MEETING_HOUR or MAX_MEETING_HOUR < hour:
            return False
    return True


if __name__ == "__main__":
    timezones_ = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']
    print(within_schedule(datetime(2018, 4, 18, 13, 28), *timezones_))
    print(within_schedule(datetime(2018, 4, 18, 12, 28), *timezones_))
