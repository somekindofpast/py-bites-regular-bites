from collections import Counter

import bs4
import requests

COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""
    with requests.Session() as session:
        content = session.get(url).content.decode('utf-8')
    soup = bs4.BeautifulSoup(content, "html.parser")
    entry_point = soup.find("div", TARGET_DIV)
    email_table_rows = entry_point.find("table").find_all("tr")
    return (row.find_all("td")[2].text for row in email_table_rows)


def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()
    counter = Counter()
    for email in emails:
        domain = email.split('@')[1]
        if domain not in common_domains:
            counter[domain] += 1
    return counter.most_common()


if __name__ == '__main__':
    common_domains = list(get_common_domains())
    print(len(common_domains))
    print(common_domains)
    print(get_most_common_domains(["a@gmail.com", "b@pybit.es", "c@pybit.es", "d@domain.de"]))
    # [('pybit.es', 2), ('domain.de', 1)]