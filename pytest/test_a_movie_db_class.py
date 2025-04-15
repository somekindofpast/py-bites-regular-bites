import os
import random
import string

import pytest

from movies import MovieDb

salt = ''.join(
    random.choice(string.ascii_lowercase) for i in range(20)
)
DB = os.path.join(os.getenv("TMP", "/tmp"), f'movies_{salt}.db')
# https://www.imdb.com/list/ls055592025/
DATA = [
    ("The Godfather", 1972, 9.2),
    ("The Shawshank Redemption", 1994, 9.3),
    ("Schindler's List", 1993, 8.9),
    ("Raging Bull", 1980, 8.2),
    ("Casablanca", 1942, 8.5),
    ("Citizen Kane", 1941, 8.3),
    ("Gone with the Wind", 1939, 8.1),
    ("The Wizard of Oz", 1939, 8),
    ("One Flew Over the Cuckoo's Nest", 1975, 8.7),
    ("Lawrence of Arabia", 1962, 8.3),
]
TABLE = 'movies'


@pytest.fixture(scope="function")
def db(request):
    # instantiate MovieDb class using above constants
    # do proper setup / teardown using MovieDb methods
    # https://docs.pytest.org/en/latest/fixture.html (hint: yield)

    movie_db = MovieDb(DB, DATA, TABLE)
    movie_db.init()

    def fin():
        movie_db.drop_table()

    request.addfinalizer(fin)

    return movie_db


# write tests for all MovieDb's query / add / delete

def test_db_query_all(db):
    query = db.query()
    titles = [movie[1] for movie in query]
    for movie in DATA:
        assert movie[0] in titles


def test_db_query_title(db):
    query = db.query(title="the")
    assert len(query) == 5
    titles = [movie[1] for movie in query]
    assert "The Godfather" in titles
    assert "The Shawshank Redemption" in titles
    assert "Gone with the Wind" in titles
    assert "The Wizard of Oz" in titles
    assert "One Flew Over the Cuckoo's Nest" in titles


def test_db_query_year(db):
    query = db.query(year=1939)
    assert len(query) == 2
    titles = [movie[1] for movie in query]
    assert "Gone with the Wind" in titles
    assert "The Wizard of Oz" in titles


def test_db_query_score(db):
    query = db.query(score_gt=9)
    assert len(query) == 2
    titles = [movie[1] for movie in query]
    assert "The Godfather" in titles
    assert "The Shawshank Redemption" in titles


def test_db_insert(db):
    title = "new title"
    year = 2000
    score = 1.5
    db.add(title, year, score)

    query = db.query(title=title)
    assert len(query) == 1
    assert query[0][1] == title
    assert query[0][2] == year
    assert query[0][3] == score


def test_db_delete(db):
    query = db.query()
    id_to_delete = query[-1][0]

    db.delete(id_to_delete)

    query = db.query()
    ids = [movie[0] for movie in query]
    assert id_to_delete not in ids