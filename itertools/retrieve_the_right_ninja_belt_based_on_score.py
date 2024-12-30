import itertools

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()


def get_belt(user_score, scores=scores, belts=belts):
    try:
        return list(itertools.filterfalse(lambda item: user_score < item[1], itertools.zip_longest(belts, scores)))[-1][0]
    except:
        return None


if __name__ == '__main__':
    print(get_belt(9))
    print(get_belt(10))
    print(get_belt(49))
    print(get_belt(999))
    print(get_belt(1000))