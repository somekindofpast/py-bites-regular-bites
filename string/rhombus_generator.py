STAR = '*'

def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    res = []
    for i in range(1, width, 2):
        spaces = ' ' * int((width - i) / 2)
        res.append(f"{spaces}{'*' * i}{spaces}")
    return res + ['*' * width] + res[::-1]


if __name__ == '__main__':
    print(gen_rhombus(5))