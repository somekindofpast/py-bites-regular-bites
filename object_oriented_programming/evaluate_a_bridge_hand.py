from collections import namedtuple
from enum import Enum
from typing import Sequence

Suit = Enum("Suit", list("SHDC"))
Rank = Enum("Rank", list("AKQJT98765432"))
Card = namedtuple("Card", ["suit", "rank"])

HCP = {Rank.A: 4, Rank.K: 3, Rank.Q: 2, Rank.J: 1}
SSP = {2: 1, 1: 2, 0: 3}  # cards in a suit -> short suit points


def _rank_to_point(ranks: list[Rank]) -> list[int]:
    points: list[int] = []
    for rank in ranks:
        point = 10
        if rank.name.isalpha() and rank.name != 'T':
            point += HCP[rank]
        elif rank.name.isdigit():
            point = int(rank.name)
        points.append(point)
    return points

def _point_to_rank_str(points: list[int]) -> str:
    rank_str = ""
    for point in points:
        if point == 10:
            rank = 'T'
        elif point < 10:
            rank = str(point)
        else:
            rank = [str(key).split('.')[1] for key, val in HCP.items() if val == point - 10][0]
        rank_str += rank
    return rank_str


class BridgeHand:
    def __init__(self, cards: Sequence[Card]):
        """
        Process and store the sequence of Card objects passed in input.
        Raise TypeError if not a sequence
        Raise ValueError if any element of the sequence is not an instance
        of Card, or if the number of elements is not 13
        """
        if not isinstance(cards, Sequence):
            raise TypeError
        if len(cards) != 13:
            raise ValueError
        for card in cards:
            if not isinstance(card, Card):
                raise ValueError
        self.cards = cards

    def __str__(self) -> str:
        """
        Return a string representing this hand, in the following format:
        "S:AK3 H:T987 D:KJ98 C:QJ"
        List the suits in SHDC order, and the cards within each suit in
        AKQJT..2 order.
        Separate the suit symbol from its cards with a colon, and
        the suits with a single space.
        Note that a "10" should be represented with a capital 'T'
        """
        result_str = ""
        for suit in Suit:
            ranks: list[Rank] = self._get_ranks(suit)
            if len(ranks) != 0:
                points: list[int] = sorted(_rank_to_point(ranks), reverse=True)
                result_str += f" {suit.name}:"
                result_str += _point_to_rank_str(points)
        return result_str.lstrip()

    def _get_ranks(self, suit: Suit) -> list[Rank]:
        return [card.rank for card in self.cards if card.suit.name == suit.name]

    def _count_suits_by_card_num(self, card_num: int) -> int:
        suit_num = 0
        for suit in Suit:
            if len(self._get_ranks(suit)) == card_num:
                suit_num += 1
        return suit_num

    @property
    def hcp(self) -> int:
        """ Return the number of high card points contained in this hand """
        hcp = 0
        for card in self.cards:
            if card.rank.name != 'T' and not str(card.rank.name).isnumeric():
                hcp += HCP[card.rank]
        return hcp

    @property
    def doubletons(self) -> int:
        """ Return the number of doubletons contained in this hand """
        return self._count_suits_by_card_num(2)


    @property
    def singletons(self) -> int:
        """ Return the number of singletons contained in this hand """
        return self._count_suits_by_card_num(1)

    @property
    def voids(self) -> int:
        """ Return the number of voids (missing suits) contained in
            this hand
        """
        return self._count_suits_by_card_num(0)

    @property
    def ssp(self) -> int:
        """ Return the number of short suit points in this hand. """
        return self.doubletons + (self.singletons * 2) + (self.voids * 3)

    @property
    def total_points(self) -> int:
        """ Return the total points (hcp and ssp) contained in this hand """
        return self.hcp + self.ssp

    @property
    def ltc(self) -> int:
        """ Return the losing trick count for this hand - see bite description
            for the procedure
        """
        ltc = 0
        for suit in Suit:
            ranks: list[Rank] = self._get_ranks(suit)
            points: list[int] = sorted(_rank_to_point(ranks), reverse=True)
            rank_str: str = _point_to_rank_str(points)
            if len(rank_str) == 1 and rank_str != 'A':
                ltc += 1
            if len(rank_str) == 2 and rank_str != 'AK':
                if rank_str[0] == 'A' or rank_str[0] == 'K':
                    ltc += 1
                else:
                    ltc += 2
            if 3 <= len(rank_str) and rank_str[:3] != 'AKQ':
                if rank_str[0] == 'A':
                    if rank_str[1] == 'K' or rank_str[1] == 'Q':
                        ltc += 1
                    else:
                        ltc += 2
                elif rank_str[0] == 'K':
                    if rank_str[1] == 'Q':
                        ltc += 1
                    else:
                        ltc += 2
                elif rank_str[0] == 'Q':
                    ltc += 2
                else:
                    ltc += 3
        return ltc


if __name__ == '__main__':
    """_cards = [
        Card(Suit["H"], Rank["T"]), Card(Suit["H"], Rank["4"]), Card(Suit["H"], Rank["2"]), Card(Suit["H"], Rank["5"]),
        Card(Suit["S"], Rank["K"]), Card(Suit["S"], Rank["6"]), Card(Suit["S"], Rank["3"]), Card(Suit["S"], Rank["7"]),
        Card(Suit["D"], Rank["A"]), Card(Suit["D"], Rank["Q"]), Card(Suit["D"], Rank["8"]),
        Card(Suit["C"], Rank["2"]), Card(Suit["C"], Rank["3"]),
    ]"""
    _cards = [
        Card(Suit["S"], Rank["A"]), Card(Suit["S"], Rank["K"]), Card(Suit["S"], Rank["Q"]), Card(Suit["S"], Rank["J"]),
        Card(Suit["S"], Rank["T"]), Card(Suit["S"], Rank["9"]), Card(Suit["S"], Rank["8"]), Card(Suit["S"], Rank["7"]),
        Card(Suit["S"], Rank["6"]), Card(Suit["S"], Rank["5"]), Card(Suit["S"], Rank["4"]),
        Card(Suit["S"], Rank["3"]), Card(Suit["S"], Rank["2"]),
    ]
    bridge_hand = BridgeHand(_cards)
    print(bridge_hand)
    print(bridge_hand.hcp)
    print(bridge_hand.doubletons)
    print(bridge_hand.singletons)
    print(bridge_hand.voids)
    print(bridge_hand.ssp)
    print(bridge_hand.total_points)
    print(bridge_hand.ltc)