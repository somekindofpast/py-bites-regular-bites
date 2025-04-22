import os
from abc import ABC, abstractmethod
from collections import namedtuple, Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, List, Optional
from urllib.request import urlretrieve
from urllib.error import URLError

from bs4 import BeautifulSoup as Soup  # type: ignore

TMP = os.getenv("TMP", "/tmp")
TODAY = date.today()
Candidate = namedtuple("Candidate", "name votes")
LeaderBoard = namedtuple(
    "LeaderBoard", "Candidate Average Delegates Contributions Coverage"
)
Poll = namedtuple(
    "Poll",
    "Poll Date Sample Sanders Biden Gabbard Spread",
)


@dataclass(init=False)
class File:
    """File represents a filesystem path.

    Variables:
        name: str -- The filename that will be created on the filesystem.
        path: Path -- Path object created from the name passed in.

    Methods:
        [property]
        data: -> Optional[str] -- If the file exists, it returns its contents.
            If it does not exist, it returns None.
    """
    name: str
    path: Path

    def __init__(self, name):
        self.name = name
        self.path = Path(os.path.join(TMP, str(TODAY) + '_' + self.name))


    @property
    def data(self) -> Optional[str]:
        try:
            with open(self.path) as f:
                content = f.read()
            return None if not content or len(content) == 0 else content
        except:
            return None



@dataclass
class Web:
    """Web object.

    Web is an object that downloads the page from the url that is passed
    to it and stores it in the File instance that is passed to it. If the
    File already exists, it just reads the file, otherwise it downloads it
    and stores it in File.

    Variables:
        url: str -- The url of the web page.
        file: File -- The File object to store the page data into.

    Methods:
        [property]
        data: -> Optional[str] -- Reads the text from File or retrieves it from the
            web if it does not exists.

        [property]
        soup: -> Soup -- Parses the data from File and turns it into a BeautifulSoup
            object.
    """
    url: str
    file: File


    @property
    def data(self) -> Optional[str]:
        """Reads the data from the File object.

        First it checks if the File object has any data. If it doesn't, it retrieves
        it and saves it to the File. It then reads it from the File and returns it.

        Returns:
            Optional[str] -- The string data from the File object.
        """
        data = self.file.data

        if not data:
            try:
                urlretrieve(self.url, self.file.path)
                data = self.file.data
            except:
                raise URLError("urlopen error")

        return data


    @property
    def soup(self) -> Soup:
        """Converts string data from File into a BeautifulSoup object.

        Returns:
            Soup -- BeautifulSoup object created from the File.
        """
        return Soup(self.data, "html.parser")


class Site(ABC):
    """Site Abstract Base Class.

    Defines the structure for the objects based on this class and defines the interfaces
    that should be implemented in order to work properly.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        [abstractmethod]
        parse_rows: -> Union[List[LeaderBoard], List[Poll]] -- Parses a BeautifulSoup
            table element and returns the text found in the td elements as
            namedtuples.

        [abstractmethod]
        polls: -> Union[List[LeaderBoard], List[Poll]] -- Does the parsing of the table
            and rows for you. It takes the table index number if given, otherwise
            parses table 0.

        [abstractmethod]
        stats: -- Formats the results from polls into a more user friendly
            representation.
    """

    @property
    @abstractmethod
    def web(self) -> Web:
        pass


    def find_table(self, loc: int = 0) -> str:
        """Finds the table elements from the Soup object

        Keyword Arguments:
            loc {int} -- Parses the Web object for table elements and
                returns the first one that it finds unless an integer representing
                the required table is passed. (default: {0})

        Returns:
            str -- The html table
        """
        return self.web.soup.find_all("table")[loc]


    @abstractmethod
    def parse_rows(self, table: Soup) -> List[Any]:
        """Abstract Method

        Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as NamedTuple.

        Returns:
            List[NamedTuple] -- List of NamedTuple that were created from the
                table data.
        """
        pass


    @abstractmethod
    def polls(self, table: int = 0) -> List[Any]:
        """Abstract Method

        Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[NamedTuple] -- List of NamedTuple that were created from the
                table data.
        """
        pass


    @abstractmethod
    def stats(self, loc: int = 0):
        """Abstract Method

        Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.
        """
        pass


@dataclass
class RealClearPolitics(Site):
    """RealClearPolitics object.

    RealClearPolitics is a custom class to parse a Web instance from the
    realclearpolitics website.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        parse_rows: -> List[Poll] -- Parses a BeautifulSoup table element and
            returns the text found in the td elements as Poll namedtuples.

        polls: -> List[Poll] -- Does the parsing of the table and rows for you.
            It takes the table index number if given, otherwise parses table 0.

        stats: -- Formats the results from polls into a more user friendly
            representation:

            Example:

            RealClearPolitics
            =================
                Biden: 214.0
              Sanders: 142.0
              Gabbard: 6.0

    """

    def __init__(self, web: Web):
        self._web = web


    @property
    def web(self) -> Web:
        return self._web


    def parse_rows(self, table: Soup) -> List[Poll]:
        """Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as Poll namedtuples.

        Returns:
            List[Poll] -- List of Poll namedtuples that were created from the
                table data.
        """
        polls: List[Poll] = []
        rows = table.find_all("tr")
        for i in range(2, len(rows)):
            tuple_args = []
            for td in rows[i].find_all("td"):
                try:
                    val = float(td.text)
                except:
                    val = td.text
                tuple_args.append(val)
            polls.append(Poll(tuple_args[0], tuple_args[1], tuple_args[2], tuple_args[4], tuple_args[3], tuple_args[5], tuple_args[6]))
        return polls


    def polls(self, table: int = 0) -> List[Poll]:
        """Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[Poll] -- List of Poll namedtuples that were created from the
                table data.
        """
        return self.parse_rows(self.find_table(table))


    def stats(self, loc: int = 0):
        """Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.

        """
        print("RealClearPolitics")
        print(f"{'=' * 17}")
        print()
        counter = Counter()
        for poll in self.polls(loc):
            counter["Sanders"] += float(poll.Sanders) if poll.Sanders != "--" else 0.0
            counter["Biden"] += float(poll.Biden) if poll.Biden != "--" else 0.0
            counter["Gabbard"] += float(poll.Gabbard) if poll.Gabbard != "--" else 0.0
        print(f"Sanders: {counter["Sanders"]}")
        print(f"Biden: {counter["Biden"]}")
        print(f"Gabbard: {counter["Gabbard"]}")
        print()


@dataclass
class NYTimes(Site):
    """NYTimes object.

    NYTimes is a custom class to parse a Web instance from the nytimes website.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        parse_rows: -> List[LeaderBoard] -- Parses a BeautifulSoup table element and
            returns the text found in the td elements as LeaderBoard namedtuples.

        polls: -> List[LeaderBoard] -- Does the parsing of the table and rows for you.
            It takes the table index number if given, otherwise parses table 0.

        stats: -- Formats the results from polls into a more user friendly
            representation:

            Example:

            NYTimes
            =================================

                               Pete Buttigieg
            ---------------------------------
            National Polling Average: 10%
                   Pledged Delegates: 25
            Individual Contributions: $76.2m
                Weekly News Coverage: 3

    """

    def __init__(self, web: Web):
        self._web = web


    @property
    def web(self) -> Web:
        return self._web


    def parse_rows(self, table: Soup) -> List[LeaderBoard]:
        """Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as LeaderBoard namedtuples.

        Returns:
            List[LeaderBoard] -- List of LeaderBoard namedtuples that were created from
            the table data.
        """
        leaderboard: List[LeaderBoard] = []
        rows = table.find_all("tr")
        for i in range(1, 4):
            cells = rows[i].find_all("td")
            candidate = cells[0].find_all("span")[1].text
            average = cells[1].find_all("span")[0].text
            delegates = int(cells[2].find_all("span")[0].text)
            contributors = cells[3].find_all("span")[0].text
            coverage = int(cells[4].find_all("span")[0].text.lstrip('#'))

            leaderboard.append(LeaderBoard(candidate, average, delegates, contributors, coverage))
        return leaderboard


    def polls(self, table: int = 0) -> List[LeaderBoard]:
        """Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[LeaderBoard] -- List of LeaderBoard namedtuples that were created from
                the table data.
        """
        return self.parse_rows(self.find_table(table))


    def stats(self, loc: int = 0):
        """Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.
        """
        print(f"{'=' * 33}")
        print(f"{'-' * 33}")
        for pol in self.polls(loc):
            print(f"National Polling Average: {pol.Average}")
            print(f"       Pledged Delegates: {pol.Delegates}")
            print(f"Individual Contributions: {pol.Contributions}")
            print(f"    Weekly News Coverage: {pol.Coverage}")


def gather_data():
    rcp_file = File("realclearpolitics.html")
    rcp_url = (
        "https://bites-data.s3.us-east-2.amazonaws.com/2020-03-10_realclearpolitics.html"
    )
    rcp_web = Web(rcp_url, rcp_file)
    rcp = RealClearPolitics(rcp_web)
    rcp.stats(3)

    nyt_file = File("nytimes.html")
    nyt_url = (
        "https://bites-data.s3.us-east-2.amazonaws.com/2020-03-10_nytimes.html"
    )
    nyt_web = Web(nyt_url, nyt_file)
    nyt = NYTimes(nyt_web)
    nyt.stats()


if __name__ == "__main__":
    gather_data()