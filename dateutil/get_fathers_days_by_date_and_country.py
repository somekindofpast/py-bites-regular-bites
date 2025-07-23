import os
from pathlib import Path
from urllib.request import urlretrieve

from dateutil.parser import parse

DEFAULT_YEAR = 2020

# get the data
TMP = Path(os.getenv("TMP", "/tmp"))
base_url = 'https://bites-data.s3.us-east-2.amazonaws.com/'

fathers_days_countries = TMP / 'fathers-day-countries.txt'
fathers_days_recurring = TMP / 'fathers-day-recurring.txt'

for file_ in (fathers_days_countries, fathers_days_recurring):
    if not file_.exists():
        urlretrieve(base_url + file_.name, file_)


def _parse_father_days_per_country(year, filename=fathers_days_countries):
    """Helper to parse fathers_days_countries"""
    with open(filename) as f:
        lines = f.readlines()

    father_dates = {}
    states = []
    for line in lines:
        if line.startswith('*'):
            line = line.strip().lstrip('*').replace(" and ", " ")
            states = [state.strip() for state in line.split(',')]
        elif line.startswith(str(year)):
            date_str = line.split(": ")[1].strip()
            father_dates[date_str] = states
    return father_dates


def _parse_recurring_father_days(filename=fathers_days_recurring):
    """Helper to parse fathers_days_recurring"""
    with open(filename) as f:
        lines = f.readlines()

    father_dates = {}
    date_str = ""
    states = []
    for i in range(1, len(lines)):
        line = lines[i].strip()
        if line.startswith('*'):
            date_str = line.lstrip('* ')
        elif line != '':
            states.append(line)

        if line == '' or i == len(lines) - 1:
            father_dates[date_str] = states
            states = []
    return father_dates


def get_father_days(year=DEFAULT_YEAR):
    """Returns a dictionary of keys = dates and values = lists
       of countries that celebrate Father's day that date

       Consider using the the 2 _parse* helpers.
    """
    father_dates = _parse_recurring_father_days()
    country_dates = _parse_father_days_per_country(year)

    for date_str in country_dates.keys():
        if date_str not in father_dates:
            father_dates[date_str] = country_dates[date_str]
        else:
            father_dates[date_str] = sorted(set(father_dates[date_str].extend(country_dates[date_str])))

    return father_dates


def generate_father_day_planning(father_days=None):
    """Prints all father days in order, example in tests and
       Bite description
    """
    if father_days is None:
        father_days = get_father_days()

    ordered_keys = sorted(father_days.keys(), key=lambda x: parse(f"{x} {DEFAULT_YEAR}"))

    for key in ordered_keys:
        print(key)
        for state in father_days[key]:
            print(f"- {state}")
        print()


if __name__ == "__main__":
    print(get_father_days(DEFAULT_YEAR))
    generate_father_day_planning()