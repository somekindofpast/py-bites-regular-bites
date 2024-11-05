IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    results: list[str] = []
    for i in range(len(names)):
        if names[i].lower()[0] == IGNORE_CHAR or 0 < len(''.join(c for c in names[i] if c.isnumeric())):
            continue
        elif names[i].lower()[0] == QUIT_CHAR or MAX_NAMES <= len(results):
            break
        results.append(names[i])
    return results


if __name__ == '__main__':
    print(filter_names(['bob', 'berta']))
    print(filter_names(['t2im', '1quinton', 'ana', '4']))
    print(filter_names(['tim', 'quinton', 'ana']))