from collections import defaultdict

names = 'bob julian tim martin rod sara joyce nick beverly kevin'.split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
               (3, 4), (4, 5), (5, 6), (5, 7), (5, 9),
               (6, 8), (7, 8), (8, 9)]


def get_friend_with_most_friends(friendships, users=users):
    """Receives the friendships list of user ID pairs,
       parse it to see who has most friends, return a tuple
       of (name_friend_with_most_friends, his_or_her_friends)"""
    friend_dict = defaultdict(list)
    for f in friendships:
        friend_dict[f[0]].append(users[f[1]])
        friend_dict[f[1]].append(users[f[0]])
    top = sorted(friend_dict.items(), key=lambda x: len(x[1]), reverse=True)[0]
    return users[top[0]], top[1]


if __name__ == '__main__':
    print(get_friend_with_most_friends(friendships))


    friendships = [(0, 1), (0, 2), (1, 2), (1, 6), (2, 3),
                   (3, 4), (4, 6), (5, 6), (5, 7), (5, 9),
                   (6, 7), (6, 8), (6, 9)]
    print(get_friend_with_most_friends(friendships))


    names = 'bob bob tim tim julian julian'.split()
    ids = range(len(names))
    users = dict(zip(ids, names))
    friendships = [(0, 1), (0, 2), (0, 4), (0, 5), (1, 3),
                   (2, 4), (4, 5)]
    print(get_friend_with_most_friends(friendships, users=users))