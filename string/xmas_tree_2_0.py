STAR = "+"
LEAF = "*"
TRUNK = "|"


def generate_improved_xmas_tree(rows=10):
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
       for given rows of leafs (default 10).
       For more information see the test and the bite description"""
    res = ""
    row_max_length = get_char_num(rows)
    for row_number in range(1, rows + 1):
        leaf_num = get_char_num(row_number)
        space_num = get_space_num(row_max_length, leaf_num)
        if res == "":
            res += get_tree_row(space_num, leaf_num, STAR)
        res += get_tree_row(space_num, leaf_num, LEAF)

    trunk_num = int(row_max_length / 2.0)
    trunk_num += 1 if trunk_num % 2 == 0 else 2
    space_num = get_space_num(row_max_length, trunk_num)
    res += get_tree_row(space_num, trunk_num, TRUNK)
    res += get_tree_row(space_num, trunk_num, TRUNK)
    return res.rstrip()


def get_char_num(row_number) -> int:
    return row_number * 2 - 1


def get_space_num(row_max_length: int, character_num: int) -> int:
    return int((row_max_length - character_num) / 2)


def get_tree_row(space_num: int, character_num: int, character: str) -> str:
    return ''.join(' ' * space_num) + ''.join(character * character_num) + ''.join(' ' * space_num) + '\n'