import os
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)


def create_chart():
    with open(SAFARI_LOGS, 'r') as f:
        lines = f.readlines()

    date = ""
    for i in range(len(lines)):
        if "sending to slack channel" in lines[i]:
            new_date = lines[i].split()[0]
            if date != new_date:
                if date:
                    print("\n", end='')
                print(new_date + ' ', end='')
                date = new_date
            if "python" in lines[i - 1].lower():
                print(PY_BOOK, end='')
            else:
                print(OTHER_BOOK, end='')

if __name__ == '__main__':
    create_chart()