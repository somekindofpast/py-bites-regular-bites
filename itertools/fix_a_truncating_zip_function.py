import itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


def get_attendees():
    [print(item) for item in itertools.zip_longest(names, locations, confirmed, fillvalue='-')]


if __name__ == '__main__':
    get_attendees()