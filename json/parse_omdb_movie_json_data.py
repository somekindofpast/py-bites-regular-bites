import json
import os
from collections import Counter
from pathlib import Path
from urllib.request import urlretrieve

TMP = Path(os.getenv("TMP", "/tmp"))
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DATA = 'omdb_data'

DATA_LOCAL = TMP / DATA
if not Path(DATA_LOCAL).exists():
    urlretrieve(S3 + DATA, DATA_LOCAL)


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    results: list[dict] = []
    for file in files:
        with open(file, 'r') as f_:
            contents = f_.readlines()
        results.append(json.loads("".join(contents)))
    return results


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    return next(movie["Title"] for movie in movies if "comedy" in movie["Genre"].lower())


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    counter = Counter()
    for movie in movies:
        counter[movie["Title"]] = int(str(movie["Awards"]).split()[-2])
    return counter.most_common(1)[0][0]


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    counter = Counter()
    for movie in movies:
        counter[movie["Title"]] = int(str(movie["Runtime"]).split()[0])
    return counter.most_common(1)[0][0]


if __name__ == '__main__':
    files_ = []
    with open(DATA_LOCAL) as f:
        for i, line in enumerate(f.readlines(), 1):
            movie_json = TMP / f'{i}.json'
            with open(movie_json, 'w') as f2:
                f2.write(f'{line}\n')
            files_.append(movie_json)

    movies_ = get_movie_data(files_)

    # teardown
    for file_ in files_:
        file_.unlink()

    for movie_ in movies_:
        print(movie_)

    print(get_single_comedy(movies_))
    print(get_movie_most_nominations(movies_))
    print(get_movie_longest_runtime(movies_))