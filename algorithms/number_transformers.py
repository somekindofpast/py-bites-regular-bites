def num_ops(n):
    """
    Input: an integer number, the target number
    Output: the minimum number of operations required to reach to n from 1.

    Two operations rules:
    1.  multiply by 2
    2.  int. divide by 3

    The base number is 1. Meaning the operation will always start with 1
    These rules can be run in any order, and can be run independently.

    [Hint] the data structure is the key to solve it efficiently.
    """

    attempts = [(1, 0)]
    dictionary = {1: 0}
    while True:
        attempts_next = []
        for att in attempts:
            if att[0] == n:
                return att[1]

            att_next = att[1] + 1
            mult = att[0] * 2
            div = int(att[0] / 3)

            if mult not in dictionary:
                attempts_next.append((mult, att_next))
                dictionary[mult] = att_next

            if div != 0 and div not in dictionary:
                attempts_next.append((div, att_next))
                dictionary[div] = att_next

        attempts.clear()
        attempts = attempts_next


print(num_ops(3012))