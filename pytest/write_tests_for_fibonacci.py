import pytest

from fibonacci import fib

# write one or more pytest functions below, they need to start with test_

def test_below_zero():
    with pytest.raises(ValueError):
        fib(-1)

@pytest.mark.parametrize("data, expected", [
    (0, 0), (1, 1)
])
def test_zero_and_one(data, expected):
    assert fib(data) == expected

@pytest.mark.parametrize("data, expected", [
    (2, 1), (3, 2), (5, 5)
])
def test_higher_numbers(data, expected):
    assert fib(data) == expected