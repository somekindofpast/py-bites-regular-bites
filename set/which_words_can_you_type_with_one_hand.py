from enum import Enum


class Hand(str, Enum):
    RIGHT = "right"
    LEFT = "left"
    BOTH = "both"


LEFT_HAND_CHARS = set("QWERTASDFGZXCVB")
RIGHT_HAND_CHARS = set("YUIOPHJKLNM")


def get_hand_for_word(word: str) -> Hand:
    """
    Use the LEFT_HAND_CHARS and RIGHT_HAND_CHARS sets to determine
    if the passed in word can be written with only the left or right
    hand, or if both hands are needed.
    """
    result: Hand
    for i in range(len(word)):
        c = word[i].upper()
        current_char_hand = Hand.LEFT if c in LEFT_HAND_CHARS else Hand.RIGHT
        if i == 0:
            result = current_char_hand
        elif current_char_hand != result:
            return Hand.BOTH
    return result