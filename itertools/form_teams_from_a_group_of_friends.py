import itertools


def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        return itertools.permutations(friends, team_size)
    else:
        return itertools.combinations(friends, team_size)


if __name__ == '__main__':
    friends_ = 'Bob Dante Julian Martin'.split()
    print(list(friends_teams(friends_, order_does_matter=True)))
    print(list(friends_teams(friends_, order_does_matter=False)))