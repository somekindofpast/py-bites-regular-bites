from random import choice

defeated_by = dict(paper='scissors',
                   rock='paper',
                   scissors='rock')
lose = '{} beats {}, you lose!'
win = '{} beats {}, you win!'
tie = 'tie!'


def _get_computer_move():
    """Randomly select a move"""
    return choice(list(defeated_by.values()))


def _get_winner(computer_choice, player_choice):
    """Return above lose/win/tie strings populated with the
       appropriate values (computer vs player)"""
    if defeated_by[player_choice] == computer_choice:
        return lose.format(computer_choice, player_choice)
    elif defeated_by[computer_choice] == player_choice:
        return win.format(player_choice, computer_choice)
    return tie


def game():
    """Game loop, receive player's choice via the generator's
       send method and get a random move from computer (_get_computer_move).
       Raise a StopIteration exception if user value received = 'q'.
       Check who wins with _get_winner and print its return output."""
    while True:
        value = yield
        if value == 'q':
            raise StopIteration
        elif value not in defeated_by.keys():
            print("Invalid")
        else:
            print(_get_winner(_get_computer_move(), value))