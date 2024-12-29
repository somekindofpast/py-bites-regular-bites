import itertools


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    count = 0
    results: [float] = []
    for item in itertools.accumulate(sequence):
        count += 1
        results.append(float(f"{(item / count):.2f}"))
    return results


if __name__ == '__main__':
    print(list(running_mean([1, 2, 3])))
    print(list(running_mean([2, 6, 10, 8, 11, 10])))
    print(list(running_mean([3, 4, 6, 2, 1, 9, 0, 7, 5, 8])))
    print(list(running_mean([])))