from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    results = [PYBITES_BORN]
    for _ in range(10):
        results.append(results[-1] + timedelta(days=100))
    return results[1:]


if __name__ == '__main__':
    print(gen_special_pybites_dates())