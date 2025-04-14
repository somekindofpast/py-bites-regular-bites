from unittest.mock import patch

import pytest

from guess import GuessGame, InvalidNumber


# write test code to reach coverage + make mutatest happy

def test_invalid_input():
    with pytest.raises(InvalidNumber):
        GuessGame("not a number")
    with pytest.raises(InvalidNumber):
        GuessGame(-1)
    with pytest.raises(InvalidNumber):
        GuessGame(16)


@patch("guess.input")
def test_lose_game(mock_input, capfd):
    secret_number = 1
    guess_game = GuessGame(secret_number, 1)
    mock_input.side_effect = ["not a number", "2"]
    guess_game()
    actual = capfd.readouterr()[0].split('\n')
    assert actual[0] == "Guess a number: "
    assert actual[1] == "Enter a number, try again"
    assert actual[2] == "Guess a number: "
    assert actual[3] == "Too high"
    assert actual[4] == f"Sorry, the number was {secret_number}"
    assert mock_input.call_count == 2


@patch("guess.input")
def test_win_game(mock_input, capfd):
    secret_number = 8
    guess_game = GuessGame(secret_number)
    mock_input.side_effect = ["4", "7", "12", "9", "8"]
    guess_game()
    actual = capfd.readouterr()[0].split('\n')
    assert actual[0] == "Guess a number: "
    assert actual[1] == "Too low"
    assert actual[2] == "Guess a number: "
    assert actual[3] == "Too low"
    assert actual[4] == "Guess a number: "
    assert actual[5] == "Too high"
    assert actual[6] == "Guess a number: "
    assert actual[7] == "Too high"
    assert actual[8] == "Guess a number: "
    assert actual[9] == "You guessed it!"
    assert mock_input.call_count == 5
