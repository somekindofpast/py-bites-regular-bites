WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    for i in range(size):
        if i % 2 == 0:
            print_pattern(WHITE + BLACK, int(size / 2))
        else:
            print_pattern(BLACK + WHITE, int(size / 2))

def print_pattern(pattern: str, repetition: int):
    print(pattern * repetition)


if __name__ == '__main__':
    create_chessboard()