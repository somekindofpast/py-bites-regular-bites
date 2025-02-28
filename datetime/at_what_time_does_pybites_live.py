from datetime import datetime
from zoneinfo import ZoneInfo

AUSTRALIA = ZoneInfo('Australia/Sydney')
SPAIN = ZoneInfo('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt: datetime):
    """
    Receives a naive UTC datetime object and returns a two element
    tuple of Australian and Spanish (timezone aware) datetimes
    https://docs.python.org/3/library/datetime.html#aware-and-naive-objects
    """
    return naive_utc_dt.astimezone(AUSTRALIA), naive_utc_dt.astimezone(SPAIN)