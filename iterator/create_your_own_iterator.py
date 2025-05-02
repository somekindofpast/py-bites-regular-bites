from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    def __init__(self, limit: int):
        self.limit = limit
        self.next_pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_pos == self.limit:
            self.next_pos = 0
            raise StopIteration
        value = choice(COLORS) + " egg"
        self.next_pos += 1
        return value