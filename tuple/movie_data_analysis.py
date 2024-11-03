import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = os.getenv("TMP", "/tmp")

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
stuff = urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')

with open(stuff[0], newline='', encoding='UTF-8') as csvfile:
    list_of_dict = list(csv.DictReader(csvfile))


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    directors = defaultdict(list)
    for row in list_of_dict:
        if row["director_name"] and row["movie_title"] and row["title_year"] and row["imdb_score"] and MIN_YEAR <= int(row["title_year"]):
            movie_title = row["movie_title"].strip("\xa0")
            directors[row["director_name"]].append(Movie(movie_title, row["title_year"], row["imdb_score"]))
    return directors


def calc_mean_score(movies: list[Movie]):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    if movies is None or len(movies) == 0:
        return 0.0
    score = 0
    for movie in movies:
        score += float(movie.score)
    return round(score / len(movies), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    director_averages: [(str, float)] = []
    for item in directors.items():
        if MIN_MOVIES <= len(item[1]):
            director_averages.append((item[0], calc_mean_score(item[1])))
    return sorted(director_averages, key=lambda tup: tup[1], reverse=True)


movies_ = get_movies_by_director()
print(movies_["Lowell Sherman"]) # should be empty

print(movies_["Frank Capra"])
print(calc_mean_score(movies_["Frank Capra"]))

print(movies_["Christopher Nolan"])
print(calc_mean_score(movies_["Christopher Nolan"]))

print(get_average_scores(movies_))