def get_index_different_char(chars):
    alphanums = set()
    non_alphanums = set()
    for i in range(len(chars)):
        if str(chars[i]).isalnum():
            alphanums.add(chars[i])
        else:
            non_alphanums.add(chars[i])
    if len(alphanums) < len(non_alphanums):
        return chars.index(alphanums.pop())
    else:
        return chars.index(non_alphanums.pop())


if __name__ == '__main__':
    tests = [
        ['A', 'f', '.', 'Q', 2],
        ['.', '{', ' ^', '%', 'a'],
        [1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'],
        ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'],
        list(range(1, 9)) + ['}'] + list('abcde'),
        [2, '.', ',', '!'],
    ]
    for test_list in tests:
        print(get_index_different_char(test_list))