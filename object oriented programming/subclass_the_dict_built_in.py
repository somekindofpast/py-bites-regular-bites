from datetime import date

MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __setitem__(self, name: str, birthday: date):
        for item in dict.items(self):
            if item[1].month == birthday.month and item[1].day == birthday.day:
                print(MSG.format(name))
                break
        dict.__setitem__(self, name, birthday)


if __name__ == '__main__':
    bd = BirthdayDict()
    bd['bob'] = date(1987, 6, 15)
    bd['tim'] = date(1984, 7, 15)
    bd['mike'] = date(1981, 7, 15)