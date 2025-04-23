def transpose(data):
    """Transpose a data structure
    1. dict
    data = {'2017-8': 19, '2017-9': 13}
    In:  transpose(data)
    Out: [('2017-8', '2017-9'), (19, 13)]

    2. list of (named)tuples
    data = [Member(name='Bob', since_days=60, karma_points=60,
                   bitecoin_earned=56),
            Member(name='Julian', since_days=221, karma_points=34,
                   bitecoin_earned=78)]
    In: transpose(data)
    Out: [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)]
    """
    if isinstance(data, dict):
        return data.keys(), data.values()

    data = [list(element) for element in data]
    result = []
    for i in range(len(data[0])):
        result.append([])
    for item in data:
        for i in range(len(item)):
            result[i].append(item[i])
    return tuple(result)


if __name__ == '__main__':
    from collections import namedtuple
    from random import randint

    def _gen_community(names):
        for name in names:
            yield Member(name=name,
                         since_days=randint(1, 365),
                         karma_points=randint(1, 100),
                         bitecoin_earned=randint(1, 100))

    POSTS = {'2017-8': 19, '2017-9': 13, '2017-10': 13,
             '2017-11': 12, '2017-12': 11, '2018-1': 3}
    NAMES = ['Bob', 'Julian', 'Tim', 'Carmen', 'Henk', 'Sofia', 'Bernard']
    Member = namedtuple('Member', 'name since_days karma_points bitecoin_earned')

    print(transpose(POSTS))
    print(transpose(list(_gen_community(NAMES))))