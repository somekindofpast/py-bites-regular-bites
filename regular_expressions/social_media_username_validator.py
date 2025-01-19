# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


def parse_social_platforms_string():
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    info = []
    all_validators = {}
    for line in social_platforms.splitlines():
        line = line.strip()
        if len(line) != 0:
            info.append(line)
        if len(info) == 4:
            range_obj = range(int(info[1].split()[1]), int(info[2].split()[1]))
            pattern_str = r"^["
            allowed_chars = info[3].split()
            for i in range(2, len(allowed_chars)):
                pattern_str += allowed_chars[i]
            pattern_str += "]+$"
            all_validators[info[0]] = Validator(range_obj, re.compile(pattern_str))
            info = []
    return all_validators


def validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()
    if platform not in all_validators:
        raise ValueError
    validator = all_validators[platform]
    return (validator.range[0] <= len(username) <= validator.range[-1]) and validator.regex.match(username) is not None


if __name__ == "__main__":
    print(parse_social_platforms_string())

    print(validate_username('Twitter', 'a'))
    print(validate_username('Twitter', ''))
    print(validate_username('Twitter', 'a'*16))

    print(validate_username('Twitter', 'bo__89A'))
    print(validate_username('Twitter', 'bob.'))