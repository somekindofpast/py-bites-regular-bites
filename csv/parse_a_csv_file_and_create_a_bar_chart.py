import csv
from collections import Counter

import requests

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    with requests.Session() as session:
        content = session.get(CSV_URL).content.decode('utf-8')

    return content


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    reader = csv.DictReader(content.splitlines(), delimiter=',')

    counter = Counter()
    max_len = 0
    for row in reader:
        counter[row["tz"]] += 1
        if max_len < len(row["tz"]):
            max_len = len(row["tz"])


    for item in sorted(counter.items()):
        space_num = max_len - len(item[0]) + 1
        spaces = ''.join(' ' * space_num)
        plus_signs = ''.join('+' * int(item[1]))
        print(f"{item[0]}{spaces}| {plus_signs}")


if __name__ == '__main__':
    create_user_bar_chart(get_csv())