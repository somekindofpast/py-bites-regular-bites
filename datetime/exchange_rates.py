import json
import os
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Dict, List, OrderedDict
from urllib.request import urlretrieve

URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
TMP = Path(os.getenv("TMP", "/tmp"))
RATES_FILE = TMP / "exchangerates.json"

if not RATES_FILE.exists():
    urlretrieve(URL, RATES_FILE)


def get_all_days(start_date: date, end_date: date) -> List[date]:
    cur_date = start_date
    res = []
    while cur_date <= end_date:
        res.append(cur_date)
        cur_date += timedelta(days=1)
    return res


def match_daily_rates(start: date, end: date, daily_rates: dict) -> Dict[date, date]:
    days = get_all_days(start, end)
    res: Dict[date, date] = OrderedDict()
    for day in days:
        cur_date = day
        while str(cur_date) not in daily_rates:
            cur_date -= timedelta(days=1)
        res[day] = cur_date
    return res


def exchange_rates(
    start_date: str = "2020-01-01", end_date: str = "2020-09-01"
) -> Dict[date, dict]:
    format_str = '%Y-%m-%d'
    start = datetime.strptime(start_date, format_str).date()
    end = datetime.strptime(end_date, format_str).date()
    rates_dict = json.loads(RATES_FILE.read_text())
    daily_rates = rates_dict["rates"]

    if not (
            datetime.strptime(rates_dict["start_at"], format_str).date() <= start <= end <= datetime.strptime(rates_dict["end_at"], format_str).date()
    ):
        raise ValueError

    matched_dates = match_daily_rates(start, end, daily_rates)

    res: Dict[date, dict] = OrderedDict()
    for key in matched_dates.keys():
        res[key] = daily_rates[str(matched_dates[key])]
        res[key]["Base Date"] = matched_dates[key]
    return res


if __name__ == '__main__':
    _daily_rates = json.loads(RATES_FILE.read_text())["rates"]
    print(get_all_days(date(2020, 4, 12), date(2020, 4, 14)))
    print(match_daily_rates(date(2020, 1, 1), date(2020, 9, 1), _daily_rates))
    print(exchange_rates())