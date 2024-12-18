from datetime import date, timedelta


TODAY = date(2020, 7, 9)


def tomorrow(today=TODAY):
    # Your code goes here
    return today + timedelta(days=1)


if __name__ == '__main__':
    print(tomorrow())
    print(tomorrow(date(2019, 12, 31)))