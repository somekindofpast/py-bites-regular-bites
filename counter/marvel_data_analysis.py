from collections import Counter, defaultdict
import csv
import re
import requests
from typing import NamedTuple


class Character(NamedTuple):
    pid: str
    name: str
    sid: str
    align: str
    sex: str
    appearances: str
    year: str


MARVEL_CSV = "https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv"  # noqa E501


def _get_csv_data() -> str:
    """Download the Marvel CSV data and return its decoded content as a string.

    Returns:
        str: The raw CSV data content as a UTF-8 decoded string.
    """
    with requests.Session() as session:
        return session.get(MARVEL_CSV).content.decode("utf-8")


def _load_data() -> list[Character]:
    """Convert the Marvel CSV data into a list of Character namedtuples.

    Returns:
        list[Character]: A list of Character namedtuples parsed from the CSV file.
    """
    content = _get_csv_data()
    reader = csv.DictReader(content.splitlines(), delimiter=",")
    characters = [
        Character(
            pid=row["page_id"],
            name=re.sub(r"(.*?)\(.*", r"\1", row["name"]).strip(),
            sid=row["ID"],
            align=row["ALIGN"],
            sex=row["SEX"],
            appearances=row["APPEARANCES"],
            year=row["Year"],
        )
        for row in reader
    ]
    return characters


characters = _load_data()


def most_popular_characters(
    characters: list[Character] = characters, top: int = 5
) -> list[str]:
    """Get the most popular characters by the number of appearances.

    Args:
        characters (list[Character]): The list of Character namedtuples.
        top (int): The number of top characters to return. Defaults to 5.

    Returns:
        list[str]: A list of names of the top `n` most popular characters.
    """
    counter = Counter()
    for character in characters:
        appearances = 0 if character.appearances == '' else int(character.appearances)
        if counter[character.name] < appearances:
            counter[character.name] = appearances
    return [tup[0] for tup in counter.most_common(top)]


def max_and_min_years_new_characters(
    characters: list[Character] = characters,
) -> tuple[str, str]:
    """Determine the years with the most and the least new Marvel characters introduced.

    In cases where multiple years have the same number of new characters,
    the most recent year is chosen.

    Args:
        characters (list[Character]): The list of Character namedtuples.

    Returns:
        tuple[str, str]: A tuple containing the year with the most and the year with the least new characters.
    """
    counter = Counter()
    for character in characters:
        if character.year:
            counter[character.year] += 1
    return counter.most_common()[0][0], counter.most_common()[-1][0]


def get_percentage_female_characters(characters: list[Character] = characters) -> float:
    """Calculate the percentage of female characters across all appearances.

    Characters without a specified gender (i.e., missing or other) are ignored.

    Args:
        characters (list[Character]): The list of Character namedtuples.

    Returns:
        float: The percentage of female characters, rounded to two decimal places.
    """
    counter = Counter()
    all_chars: defaultdict = defaultdict(list)
    for character in characters:
        if character.sex == "Female Characters":
            counter["female"] += 1
        if character.sex:
            all_chars[f"{character.pid} {character.name}"].append(character.sex)
    percentage = float(counter["female"]) / float(len(all_chars.items()))
    return float(f"{percentage:.2%}"[:-1])


if __name__ == '__main__':
    print(most_popular_characters())
    print(max_and_min_years_new_characters())
    print(get_percentage_female_characters())