from collections import namedtuple
from datetime import datetime

Transaction = namedtuple(
    'Transaction',
    'giver points date',
    defaults=(None, None, datetime.now()))


class User:
    def __init__(self, name: str):
        self.name = name
        self._transactions: list[Transaction] = []

    @property
    def karma(self) -> int:
        karma = 0
        for t in self._transactions:
            if isinstance(t.points, int):
                karma += t.points
        return karma

    @property
    def points(self) -> list[int]:
        return [t.points for t in self._transactions if isinstance(t.points, int)]

    @property
    def fans(self) -> int:
        return len({t.giver.name for t in self._transactions if isinstance(t.giver, User) and isinstance(t.giver.name, str)})

    def __add__(self, other):
        if not isinstance(other, Transaction):
            return
        self._transactions.append(other)

    def __str__(self):
        fans = self.fans
        return f'{self.name} has a karma of {self.karma} and {fans} {"fan" if fans == 1 else "fans"}'


if __name__ == '__main__':
    alice = User("alice")
    bob = User("bob")
    tim = User("tim")
    transactions = [
        Transaction(giver=alice, points=1),
        Transaction(giver=bob, points=2),
        Transaction(giver=tim, points=3),
        Transaction(giver=tim, points=4),
        Transaction(giver=alice, points=2),
    ]

    alice + transactions[1]
    assert alice.karma == 2
    alice + transactions[2]
    assert alice.karma == 5
    alice + transactions[3]
    assert alice.karma == 9
    assert alice.points == [2, 3, 4]
    assert alice.fans == 2
    assert str(alice) == 'alice has a karma of 9 and 2 fans'
    print(alice)