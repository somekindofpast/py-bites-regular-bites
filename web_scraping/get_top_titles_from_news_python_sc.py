from collections import namedtuple

from bs4 import BeautifulSoup
import requests

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)

    title_spans = soup.find_all("span", class_="title")
    titles = []
    for title_span in title_spans:
        title = title_span.find("a").text
        web_page = title_span.find("span", class_="smaller")
        if web_page:
            title += f' ({web_page.find("a").text})'
        titles.append(title)

    info_spans = soup.find_all("span", class_="controls")
    for i in range(len(info_spans)):
        points = int(info_spans[i].find("span", class_="smaller").text.strip().split(' ')[0])
        comments = int(info_spans[i].find("span", class_="naturaltime").find("a").text.strip().split(' ')[0])
        titles[i] = Entry(titles[i], points, comments)

    return sorted(titles, key=lambda tup: (tup.points, tup.comments), reverse=True)[:top]


if __name__ == '__main__':
    print(get_top_titles("https://bites-data.s3.us-east-2.amazonaws.com/"
            "news.python.sc/index.html"))
    print(get_top_titles("https://bites-data.s3.us-east-2.amazonaws.com/"
         "news.python.sc/index2.html"))