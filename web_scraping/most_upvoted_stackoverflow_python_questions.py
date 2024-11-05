import re
from collections import namedtuple

import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'

Question = namedtuple("Question", ["question", "num_votes"])

def load_page(url):
    with requests.Session() as session:
        return session.get(url).content.decode('utf-8')


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    top_questions: [Question] = []
    content = load_page(url)
    soup = BeautifulSoup(content, "html.parser")
    entry_point = soup.find("div", id="questions")
    questions = entry_point.find_all("div", {"class":"question-summary"})
    for question in questions:
        view_count = question.find("div", {"class":re.compile("^views")})
        if int(view_count.attrs["title"].split()[0].replace(",","")) < 1000000:
            continue
        vote_count = question.find("span", {"class":re.compile("^vote-count")})
        num_votes = int(vote_count.find("strong").text)
        summary = question.find("div", class_="summary")
        question_text = summary.find("a").text
        top_questions.append(Question(question_text, num_votes))
    return sorted(top_questions, key=lambda tup: tup.num_votes, reverse=True)


if __name__ == '__main__':
    print(top_python_questions())