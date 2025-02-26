def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    return len(set(my_cities) ^ set(other_cities))


if __name__ == "__main__":
    print(uncommon_cities(["a", "b", "c"], ["b", "c", "d"]))