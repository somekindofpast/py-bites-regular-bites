THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs:
    def __mul__(self, other: int) -> str:
        if other == 0:
            raise ValueError("Specify a number")
        thumb = THUMBS_UP if 0 < other else THUMBS_DOWN
        return thumb * abs(other) if -4 < other < 4 else f"{thumb} ({abs(other)}x)"

    def __rmul__(self, other):
        return self * other


if __name__ == '__main__':
    thumbs = Thumbs()
    print(thumbs * 3)
    print(-2 * thumbs)
    print(8 * thumbs)
    print(thumbs * -101)