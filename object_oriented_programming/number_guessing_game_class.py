import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        #print("Guess a number between 1 and 20: ")
        input1 = input()

        try:
            num = int(input1)
        except:
            if not input1 or input1 == '':
                print("Please enter a number")
            else:
                print("Should be a number")
            raise ValueError

        if not (START <= num <= END):
            print("Number not in range")
            raise ValueError
        if num in self._guesses:
            print("Already guessed")
            raise ValueError

        self._guesses.add(num)
        return num

    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        if guess < self._answer:
            print(f"{guess} is too low")
            return False
        elif self._answer < guess:
            print(f"{guess} is too high")
            return False
        else:
            print(f"{guess} is correct!")
            return True

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        while True:
            try:
                num = self.guess()
            except:
                continue

            if self._validate_guess(num):
                self._win = True
                print(f"It took you {len(self._guesses)} guesses")
                break
            elif MAX_GUESSES <= len(self._guesses):
                print(f"Guessed {MAX_GUESSES} times, answer was {self._answer}")
                break


if __name__ == '__main__':
    game = Game()
    game()