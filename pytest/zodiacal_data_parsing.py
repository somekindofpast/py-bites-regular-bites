from datetime import datetime
import json
import os
from pathlib import Path
from urllib.request import urlretrieve

import pytest

from zodiac import (get_signs, get_sign_with_most_famous_people,
                    signs_are_mutually_compatible, get_sign_by_date)

# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "zodiac.json")


@pytest.fixture(scope='module')
def signs():
    if not PATH.exists():
        urlretrieve(URL, PATH)
    with open(PATH) as f:
        data = json.loads(f.read())
    return get_signs(data)

# write your pytest code here ...

def test_get_sign_with_most_famous_people(signs):
    most_famous_sign = get_sign_with_most_famous_people(signs)
    assert most_famous_sign[1] == 35
    assert most_famous_sign[0] == "Scorpio" or most_famous_sign[0] == "Capricorn"


def test_signs_are_mutually_compatible(signs):
    assert signs_are_mutually_compatible(signs, "Leo", "Virgo") is False
    assert signs_are_mutually_compatible(signs, "Aries", "Gemini") is True


def test_get_sign_by_date(signs):
    assert get_sign_by_date(signs, datetime(year=1999, month=2, day=19)) == "Pisces"
    assert get_sign_by_date(signs, datetime(year=1999, month=3, day=20)) == "Pisces"