from collections import namedtuple, Counter
import re
from datetime import timedelta
from typing import NamedTuple

import feedparser

SPECIAL_GUEST = 'Special guest'

# using _ as min/max are builtins
Duration = namedtuple('Duration', 'avg max_ min_')

# static copy, original: https://pythonbytes.fm/episodes/rss
URL = 'https://bites-data.s3.us-east-2.amazonaws.com/python_bytes'
IGNORE_DOMAINS = {'https://pythonbytes.fm', 'http://pythonbytes.fm',
                  'https://twitter.com', 'https://training.talkpython.fm',
                  'https://talkpython.fm', 'http://testandcode.com'}


class PythonBytes:

    def __init__(self, url=URL):
        """Load the feed url into self.entries using the feedparser module."""
        self.entries = feedparser.parse(url)["entries"]

    def get_episode_numbers_for_mentioned_domain(self, domain: str) -> list:
        """Return a list of episode IDs (itunes_episode attribute) of the
           episodes the pass in domain was mentioned in.
        """
        return [entry['itunes_episode'] for entry in self.entries if domain in entry['description']]

    def get_most_mentioned_domain_names(self, n: int = 15) -> list:
        """Get the most mentioned domain domains. We match a domain using
           regex: "https?://[^/]+" - make sure you only count a domain once per
           episode and ignore domains in IGNORE_DOMAINS.
           Return a list of (domain, count) tuples (use Counter).
        """
        counter = Counter()
        for entry in self.entries:
            for domain_name in set(re.findall("https?://[^/]+", entry["description"])):
                if domain_name not in IGNORE_DOMAINS:
                    counter[domain_name] += 1
        return counter.most_common(n)

    def number_episodes_with_special_guest(self) -> int:
        """Return the number of episodes that had one of more special guests
           featured (use SPECIAL_GUEST).
        """
        count = 0
        for entry in self.entries:
            if SPECIAL_GUEST in entry['description']:
                count += 1
        return count

    def get_average_duration_episode_in_seconds(self) -> Duration:
        """Return the average duration in seconds of a Python Bytes episode, as
           well as the shortest and longest episode in hh:mm:ss notation.
           Return the results using the Duration namedtuple.
        """
        episode_durations: list[timedelta] = []
        for entry in self.entries:
            duration_parts = entry["itunes_duration"].split(':')
            episode_durations.append(timedelta(hours=int(duration_parts[0]), minutes=int(duration_parts[1]), seconds=int(duration_parts[2])))
        episode_durations.sort()
        average = (sum(episode_durations, timedelta(0,0)) / len(episode_durations)).seconds
        max_dur = _calc_hour_min_sec_from_timedelta(episode_durations[-1])
        min_dur = _calc_hour_min_sec_from_timedelta(episode_durations[0])
        return Duration(average, f"{max_dur[0]:>02}:{max_dur[1]:>02}:{max_dur[2]:>02}", f"{min_dur[0]:>02}:{min_dur[1]:>02}:{min_dur[2]:>02}")

def _calc_hour_min_sec_from_timedelta(time_delta: timedelta) -> tuple[int, int, int]:
    hours = time_delta.seconds // 3600
    minutes = time_delta.seconds % 3600 // 60
    seconds = time_delta.seconds - hours * 3600 - minutes * 60
    return hours, minutes, seconds

if __name__ == '__main__':
    pb = PythonBytes()
    print(pb.get_episode_numbers_for_mentioned_domain("realpython.com"))
    print(pb.get_episode_numbers_for_mentioned_domain("pybit.es"))
    print(pb.number_episodes_with_special_guest())
    print(pb.get_most_mentioned_domain_names())
    print(pb.get_average_duration_episode_in_seconds())