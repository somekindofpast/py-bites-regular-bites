def countdown():
    """Write a generator that counts from 100 to 1"""
    return (i for i in range(100, 0, -1))