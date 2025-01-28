INDENTS = 4


def print_hanging_indents(poem: str):
    paragraph_start = True
    for line in poem.strip().splitlines():
        line = line.strip()
        if line == "":
            paragraph_start = True
            continue
        elif paragraph_start:
            paragraph_start = False
        else:
            print(" " * INDENTS, end="")
        print(line)


if __name__ == '__main__':
    rosetti_unformatted = """
                          Remember me when I am gone away,
                          Gone far away into the silent land;
                          When you can no more hold me by the hand,

                          Nor I half turn to go yet turning stay.

                          Remember me when no more day by day
                          You tell me of our future that you planned:
                          Only remember me; you understand
                          """
    print_hanging_indents(rosetti_unformatted)