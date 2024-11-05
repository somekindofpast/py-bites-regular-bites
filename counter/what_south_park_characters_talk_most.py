import re
from collections import Counter, defaultdict
import csv

import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501

test_word_num = 0

def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""

    character_words = defaultdict(Counter)
    content = content.replace('Season,Episode,Character,Line\n', '')
    lines = content.splitlines()
    season_ep_char = []
    word_count = 0
    is_new_speaker = True
    for line in lines:
        line = re.sub(r'(\d),(\d{3})', r'\1_\2', line)
        if is_new_speaker:
            parts = line.split(',')
            season_ep_char.append(parts[0])
            season_ep_char.append(parts[1])
            season_ep_char.append(parts[2])
            words_start = 3
            if '"' in parts[2]:
                for i in range(words_start, len(parts)):
                    season_ep_char[-1] += parts[i]
                    if '"' in parts[i]:
                        words_start = i + 1
                        break
            for i in range(words_start, len(parts)):
                word_count += len(parts[i].strip('"').split())
            is_new_speaker = False
        else:
            if line != '"':
                word_count += len(line.split())
            else:
                character_words[season_ep_char[2]][season_ep_char[1]] += word_count
                season_ep_char = []
                word_count = 0
                is_new_speaker = True

        #TESTING
        if season_ep_char and season_ep_char[2] == "Ms. Choksondik" and season_ep_char[1] == "7" and season_ep_char[0] == "5":
            global test_word_num
            chunks = line.strip('"').split(',')
            for i in range(3, len(chunks)):
                test_word_num += len(chunks[i].strip('"').split())
                print(chunks[i].strip('"').split())
            print(line)

    return character_words


if __name__ == '__main__':
    _character_words = get_num_words_spoken_by_character_per_episode(get_season_csv_file(season=1))
    print("Stan, season 1 top 3 episodes wordcount: ", end='')
    print(_character_words['Stan'].most_common()[:3])
    print("Cartman, season 1 top 3 episodes wordcount: ", end='')
    print(_character_words['Cartman'].most_common()[:3])
    print("Cartman, season 1 bottom 3 episodes wordcount: ", end='')
    print(_character_words['Cartman'].most_common()[-3:])
    print("Bogus character, season 1 wordcount: ", end='')
    print(_character_words['Bogus'].most_common())

    _character_words = get_num_words_spoken_by_character_per_episode(get_season_csv_file(season=5))
    print("Sheila, season 5 top 3 episodes wordcount: ", end='')
    print(_character_words['Sheila'].most_common()[:3])
    print("Ms. Choksondik, season 5 top 3 episodes wordcount: ", end='')
    print(_character_words['Ms. Choksondik'].most_common()[:3])
    print(test_word_num)