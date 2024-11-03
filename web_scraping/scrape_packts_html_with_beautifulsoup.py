from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, "html.parser")
    deal_of_the_day = soup.find("div", id="deal-of-the-day")
    image = deal_of_the_day.find("img")
    image = image.attrs["src"]
    title = deal_of_the_day.find("div", class_="dotd-title")
    title = title.find("h2")
    title = title.text.strip()
    summary = deal_of_the_day.find("div", class_="dotd-main-book-summary float-left")
    divs = summary.find_all("div")
    description = divs[2].text.strip()
    link = deal_of_the_day.find("a")
    link = link.attrs["href"]
    return Book(title, description, image, link)


print(get_book())