from fizzbuzz import fizzbuzz

# write one or more pytest functions below, they need to start with test_

def test_fizz():
    assert fizzbuzz(9) == "Fizz"


def test_buzz():
    assert fizzbuzz(10) == "Buzz"


def test_fizzbuzz():
    assert fizzbuzz(15) == "Fizz Buzz"


def test_neither():
    assert fizzbuzz(16) == 16