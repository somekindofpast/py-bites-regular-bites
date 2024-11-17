def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    loops = int(abs(n) / len(string))
    offset = abs(n) - loops * len(string)
    return string[offset:] + string[:offset] if 0 < n else string[-offset:] + string[:-offset]


if __name__ == '__main__':
    print(rotate('bob and julian love pybites!', 15)) #'love pybites!bob and julian '
    print(rotate('pybites loves julian and bob!', -15))  #'julian and bob!pybites loves '