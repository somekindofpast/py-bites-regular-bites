from typing import NamedTuple
from operator import attrgetter, lt, gt


class Tweet(NamedTuple):
    text: str
    polarity: float


tweets = [
    Tweet(
        text="It's shocking that the vast majority of online banking "
        "systems have critical vulnerabilities leaving customer "
        "accounts unprotected.",
        polarity=-0.3333333333333333,
    ),
    Tweet(
        text="The most unbelievable aspect of the Star Trek universe "
        "is that every ship they meet has compatible video "
        "conferencing facilities.",
        polarity=0.125,
    ),
    Tweet(
        text="Excellent set of tips for managing a PostgreSQL cluster "
        "in production.",
        polarity=1.0,
    ),
    Tweet(
        text="This tutorial has a great line-by-line breakdown of how "
        "to train a pong RL agent in PyTorch.",
        polarity=0.8,
    ),
    Tweet(
        text="This is some masterful reporting by ... It's also an "
        "infuriating story. ... is trying to erase debt by preying "
        "on the city’s residents. The poorest get hit the worst. "
        "It’s shameful.",
        polarity=-0.19999999999999998,
    ),
]


def filter_tweets_on_polarity(
    tweets: list[Tweet], keep_positive: bool = True
) -> list[Tweet]:
    """Filter the tweets based on their polarity score.

    Args:
        tweets (list): A list of Tweet namedtuples, each with a polarity score.
        keep_positive (bool): If True, keeps only tweets with a positive polarity (polarity > 0).
                              If False, keeps only tweets with a negative polarity (polarity < 0).

    Returns:
        list: A list of tweets filtered by the specified polarity condition.
    """
    return [tweet for tweet in tweets if (0 <= tweet.polarity) is keep_positive]


def order_tweets_by_polarity(
    tweets: list[Tweet], positive_highest: bool = True
) -> list[Tweet]:
    """Sort tweets by their polarity score.

    Args:
        tweets (list): A list of Tweet namedtuples, each with a polarity score.
        positive_highest (bool): If True, sorts tweets in descending order with the highest positive polarity first.
                                 If False, sorts tweets in ascending order with the most negative polarity first.

    Returns:
        list: A list of tweets sorted by polarity according to the specified order.
    """
    return sorted(tweets, key=attrgetter("polarity"), reverse=positive_highest)