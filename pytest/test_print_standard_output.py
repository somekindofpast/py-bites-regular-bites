import pytest

from workouts import print_workout_days


def test_print_workout_days(capfd):
    print_workout_days("upper")
    actual = capfd.readouterr()[0].strip()
    assert actual == "Mon, Thu"


def test_print_workout_days_no_workout(capfd):
    print_workout_days("bogus")
    actual = capfd.readouterr()[0].strip()
    assert actual == "No matching workout"