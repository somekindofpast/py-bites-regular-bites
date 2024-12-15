from dataclasses import dataclass

from dateutil.parser import parse


@dataclass
class Actor:
    name: str
    born: str


@dataclass
class Movie:
    title: str
    release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    born_date = parse(actor.born)
    release_date = parse(movie.release_date)

    return f"{actor.name} was {int((release_date - born_date).days / 365)} years old when {movie.title} came out."


if __name__ == '__main__':
    print(get_age(Actor('Wesley Snipes', 'July 31, 1962'), Movie('New Jack City', 'January 17, 1991')))
    print(get_age(Actor('Michelle Pfeiffer', 'April 29, 1958'), Movie('Scarface', 'March 12, 1984')))