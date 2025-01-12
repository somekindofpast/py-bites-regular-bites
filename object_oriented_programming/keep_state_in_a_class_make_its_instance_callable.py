import sys


class RecordScore:
    """Class to track a game's maximum score"""
    def __init__(self):
        self.max: int = -(sys.maxsize - 1)

    def __call__(self, score: int) -> int:
        if self.max < score:
            self.max = score
        return self.max