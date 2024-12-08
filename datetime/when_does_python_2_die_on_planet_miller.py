from datetime import datetime, timedelta

# https://pythonclock.org/
PY2_DEATH_DT = datetime(year=2020, month=1, day=1)
BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')


def py2_earth_hours_left(start_date=BITE_CREATED_DT) -> float:
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""
    diff = PY2_DEATH_DT - start_date
    return float(f"{(diff.days * 24 + diff.seconds / 60 / 60):.2f}")


def py2_miller_min_left(start_date=BITE_CREATED_DT) -> float:
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)"""
    earth_years = py2_earth_hours_left(start_date) / 24 / 365
    return float(f"{(earth_years / 7 * 60):.2f}")


if __name__ == "__main__":
    print(py2_earth_hours_left())
    print(py2_miller_min_left())
    START_DATE = BITE_CREATED_DT - timedelta(days=1000)
    print(py2_earth_hours_left(START_DATE))
    print(py2_miller_min_left(START_DATE))