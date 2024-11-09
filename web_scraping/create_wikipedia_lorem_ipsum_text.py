from bs4 import BeautifulSoup
import requests
import re
from random import randint

# FEATURED_ARTICLE = ('https://en.wikipedia.org/wiki/Wikipedia:Today%27s_featured_article/January_1,_2022')
FEATURED_ARTICLE = 'https://bites-data.s3.us-east-2.amazonaws.com/wiki_features_article_2022-01-01.html'
CONTENT = requests.get(FEATURED_ARTICLE).text


def wiki_lorem_ipsum(article: str = CONTENT, number_of_sentences: int = 5) -> str:
    """Create a lorem ipsum block of sentences from the words scraped from today's Wikipedia featured article
    :param article
    :type article: str
    :param number_of_sentences
    :type number_of_sentences: int
    :return: lorem ipsum text (Lorem ipsum is nonsense text used to test layouts for documents or websites)
    rtype: str
    """
    if number_of_sentences < 1:
        raise ValueError("number of sentences set to less than one")
    soup = BeautifulSoup(article, "html.parser")
    paragraph = soup.find("div", class_="mw-parser-output").find('p')
    words = list(set(re.sub('[-,.()]', ' ', paragraph.text).lower().split()))
    sentences = ""
    for i in range(number_of_sentences):
        sentence = ""
        word_length = randint(5, 15)
        for j in range(word_length):
            sentence += words[randint(0, len(words) - 1)]
            if j < word_length - 1:
                sentence += ' '
        sentence = sentence[0].upper() + sentence[1:]
        sentence += '.'
        if i < number_of_sentences - 1:
            sentence += ' '
        sentences += sentence
    return sentences


if __name__ == '__main__':
    print(wiki_lorem_ipsum())