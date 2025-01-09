import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        try:
            self.rgb = COLOR_NAMES[str(color).upper()]
        except:
            self.rgb = None

    @staticmethod
    def hex2rgb(hex_val):
        """Class method that converts a hex value into an rgb one"""
        if not isinstance(hex_val, str):
            raise ValueError
        hex_val = hex_val.lstrip('#')
        if len(hex_val) != 6:
            raise ValueError
        return int(hex_val[0:2], 16), int(hex_val[2:4], 16), int(hex_val[4:6], 16)

    @staticmethod
    def rgb2hex(rgb_val):
        """Class method that converts an rgb value into a hex one"""
        if not isinstance(rgb_val, tuple) or len(rgb_val) != 3:
            raise ValueError
        if not isinstance(rgb_val[0], int) or rgb_val[0] < 0 or 255 < rgb_val[0]:
            raise ValueError
        if not isinstance(rgb_val[1], int) or rgb_val[1] < 0 or 255 < rgb_val[1]:
            raise ValueError
        if not isinstance(rgb_val[2], int) or rgb_val[2] < 0 or 255 < rgb_val[2]:
            raise ValueError
        return f"#{rgb_val[0]:02x}{rgb_val[1]:02x}{rgb_val[2]:02x}"

    def __repr__(self):
        """Returns the repl of the object"""
        if self.rgb is None:
            return "Color('Unknown')"
        keys = list(COLOR_NAMES.keys())
        values = list(COLOR_NAMES.values())
        position = values.index(self.rgb)
        return f"Color('{str(keys[position]).lower()}')"

    def __str__(self):
        """Returns the string value of the color object"""
        if self.rgb is None:
            return "Unknown"
        return str(self.rgb)


if __name__ == '__main__':
    print(Color("orange").rgb)
    print(Color("puke").rgb)
    print(Color.hex2rgb('#ff8000'))
    print(Color.rgb2hex((255, 128, 0)))
    print(repr(Color("brown")))
    print(repr(Color("puke")))
    print(str(Color("brown")))
    print(str(Color("puke")))