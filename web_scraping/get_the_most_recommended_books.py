from collections import Counter

from bs4 import BeautifulSoup
import requests

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')
MIN_COUNT = 3


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content=None):
    """Make a BeautifulSoup object loading in content,
       find all links that contain AMAZON, extract the book title
       (stripping spacing characters), and count them.
       Return a list of (title, count) tuples where
       count is at least MIN_COUNT
    """
    if content is None:
        content = load_page()
    soup = BeautifulSoup(content, "html.parser")
    entry_content = soup.find("div", {"class":"entry-content"})
    spans = entry_content.find_all("span")
    book_counter = Counter()
    for span in spans:
        text = span.text.strip()
        if text and len(text) != 1 and text[0] != '(':
            book_counter[text] += 1
    return [(k, v) for k, v in book_counter.items() if v >= MIN_COUNT]


print(get_top_books())