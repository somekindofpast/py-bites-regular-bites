from collections import defaultdict
import os
from urllib.request import urlretrieve
import re
from bs4 import BeautifulSoup


# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.join(tmp, page)
urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, "html.parser")
    holiday_table = soup.find("table",{"class":"list-table"})
    rows = holiday_table.find_all("tr")
    for row in rows:
        date = row.find("time")
        holiday = row.find("a")
        if date and holiday:
            month = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\2', date.text)
            holidays[month].append(holiday.text.strip())
    return holidays


print(get_us_bank_holidays(content))