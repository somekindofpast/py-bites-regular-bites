def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    res = ""
    row_length = get_star_num(rows)
    for row_number in range(1, rows + 1):
        star_num = get_star_num(row_number)
        space_num = int((row_length - star_num) / 2)
        res += ''.join(' ' * space_num) + ''.join('*' * star_num) + ''.join(' ' * space_num) + '\n'
    return res.rstrip()


def get_star_num(row_number) -> int:
    return row_number*2-1