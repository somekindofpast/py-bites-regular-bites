import itertools

def find_number_pairs(numbers, N=10):
    return list(filter(lambda x: x[0] + x[1] == N, itertools.combinations(numbers, 2)))


if __name__ == '__main__':
    print(find_number_pairs([9, 1, 3, 8, 7]))
    print(find_number_pairs([0.24, 0.36, 0.04, 0.06, 0.33, 0.08, 0.20, 0.27, 0.3, 0.31,
      0.76, 0.05, 0.08, 0.08, 0.67, 0.09, 0.66, 0.79, 0.95], 1))
    print(find_number_pairs([-9, 29, 11, 10, 9, 3, -1, 21], 20))