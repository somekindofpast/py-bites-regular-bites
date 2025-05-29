from datetime import date, timedelta

TODAY = date.today()

def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    cur_date = start_date
    while True:
        cur_date += timedelta(days=num_days)
        for _ in range(num_bites):
            yield cur_date


if __name__ == '__main__':
    from itertools import islice

    start = date(2019, 8, 25)

    gen = gen_bite_planning(num_bites=1, num_days=1, start_date=start)
    actual = list(islice(gen, 10))
    print(actual)

    gen = gen_bite_planning(num_bites=2, num_days=3, start_date=start)
    actual = list(islice(gen, 10))
    print(actual)

    gen = gen_bite_planning(num_bites=1, num_days=2, start_date=start)
    actual = list(islice(gen, 10))
    print(actual)