def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if not isinstance(rgb, tuple) or len(rgb) != 3:
        raise ValueError
    if not (0 <= rgb[0] <= 255):
        raise ValueError
    if not (0 <= rgb[1] <= 255):
        raise ValueError
    if not (0 <= rgb[2] <= 255):
        raise ValueError
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}".upper()


if __name__ == '__main__':
    print(rgb_to_hex((192,192,192)))