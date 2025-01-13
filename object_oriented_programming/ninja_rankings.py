import heapq
from dataclasses import dataclass, field
from typing import List

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass(order=True)
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """
    sort_index: int = field(init=False, repr=False)
    name: str
    bites: int

    def __post_init__(self):
        self.sort_index = self.bites

    def __str__(self):
        return f"[{self.bites}] {self.name}"


class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """
    def __init__(self):
        self.heap = []

    def add(self, other: Ninja):
        heapq.heappush(self.heap, other)
        self.heap.sort()

    def dump(self):
        lowest = heapq.heappop(self.heap)
        self.heap.sort()
        return lowest

    def highest(self, count: int = 1):
        return heapq.nlargest(count, self.heap)

    def lowest(self, count: int = 1):
        return heapq.nsmallest(count, self.heap)

    def __len__(self):
        return len(self.heap)

    def pair_up(self, count: int = 3):
        lows = self.lowest(count)
        highs = self.highest(count)
        return [pair for pair in zip(highs, lows)]


if __name__ == '__main__':
    FIRST_NINJAS = [Ninja(*ninja) for ninja in zip(names, bites)]
    rankings = Rankings()
    for ninja in FIRST_NINJAS:
        rankings.add(ninja)
    rankings.add(Ninja("test", 0))
    print(rankings.heap)
    print(len(rankings))
    print(rankings.dump())
    print(rankings.heap)
    print(len(rankings))
    print(rankings.pair_up())