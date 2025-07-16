from itertools import cycle
import sys
from time import time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports above.
       Takes seconds argument = time for the spinner to run.
       Does not return anything, only prints to stdout."""
    start = time()
    iterator = cycle(SPINNER_STATES)

    while (time() - start) < seconds:
        print(next(iterator), end='\r')
        sys.stdout.flush()
        sleep(STATE_TRANSITION_TIME)


if __name__ == '__main__':
    spinner(2)