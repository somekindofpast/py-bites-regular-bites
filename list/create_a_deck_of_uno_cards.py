from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    deck: list[UnoCard] = []
    for suit in SUITS:
        deck.append(UnoCard(suit, "0"))
        for i in range(1, 10):
            deck.append(UnoCard(suit, str(i)))
            deck.append(UnoCard(suit, str(i)))
        for name in ["Draw Two", "Skip", "Reverse"]:
            deck.append(UnoCard(suit, name))
            deck.append(UnoCard(suit, name))
    for name in ["Wild", "Wild Draw Four"]:
        for i in range(4):
            deck.append(UnoCard(None, name))
    return deck