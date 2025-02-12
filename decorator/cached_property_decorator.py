from random import random
from time import sleep


def cached_property(func):
    """decorator used to cache expensive object attribute lookup"""
    @property
    def wrapper(self, *args, **kwargs):
        if self._mass is None:
            return func(self, *args, **kwargs)
        return self._mass
    return wrapper

class Planet:
    """the nicest little orb this side of Orion's Belt"""

    GRAVITY_CONSTANT = 42
    TEMPORAL_SHIFT = 0.12345
    SOLAR_MASS_UNITS = 'M\N{SUN}'

    def __init__(self, color):
        self.color = color
        self._mass = None

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.color)})'

    @cached_property
    def mass(self):
        scale_factor = random()
        sleep(self.TEMPORAL_SHIFT)
        self._mass = (f'{round(scale_factor * self.GRAVITY_CONSTANT, 4)} '
                      f'{self.SOLAR_MASS_UNITS}')
        return self._mass


if __name__ == '__main__':
    from time import perf_counter

    blue = Planet('blue')
    start_time = perf_counter()
    for _ in range(5):
        blue.mass
    end_time = perf_counter()
    elapsed_time = end_time - start_time
    print(elapsed_time)