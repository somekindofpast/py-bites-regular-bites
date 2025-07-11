from collections import namedtuple
import random
from string import ascii_uppercase

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')

def create_paw_deck(n=8):
    if not (1 <= n <= 26):
        raise ValueError

    actions = []
    for action in ACTIONS:
        actions.extend([action for _ in range(int(n / 4))])
    random.shuffle(actions)

    paw_cards = []
    for i in range(n):
        letter = ascii_uppercase[i]
        rand_nums = random.choices([1, 2, 3, 4], k=int(n / 4))
        for num in NUMBERS:
            paw_card = PawCard(card=letter + str(num), action=None)
            if 0 < len(actions) and num in rand_nums:
                paw_card = paw_card._replace(action=actions.pop())
            paw_cards.append(paw_card)
    return paw_cards