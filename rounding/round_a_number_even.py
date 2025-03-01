import math

def round_even(number):
    """Takes a number and returns it rounded even"""
    floor: float = math.floor(number)
    mid: float = floor + 0.5
    if number < mid:
        return floor
    if mid < number:
        return math.ceil(number)
    if number == mid and floor % 2 == 0:
        return floor
    else:
        return floor + 1.0