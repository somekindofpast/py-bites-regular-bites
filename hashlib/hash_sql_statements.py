import hashlib


def hash_query(query: str, length: int = 32) -> str:
    """Return a hash value for a given query.

    Args:
        query (str): An SQL query.
        length (int, optional): Length of the hash value. Defaults to 32.

    Raises:
        ValueError: Parameter length has to be greater equal 1.
        TypeError: Parameter length has to be of type integer.

    Returns:
        str: String representation of the hashed value.
    """
    if not isinstance(length, int):
        raise TypeError
    if length < 1:
        raise ValueError

    query = query.lower().replace('"', '').rstrip(';')
    query = ' '.join(sorted(query.split()))
    h = hashlib.shake_256(query.encode('latin-1'))
    res = h.hexdigest(length)
    return res[:int(len(res) / 2)]


if __name__ == '__main__':
    from random import shuffle

    complex_query = """select Candidate, Election_year, sum(Total_$), count(*)
    from combined_party_data
    where Election_year = 2016
    group by Candidate, Election_year
    having count(*) > 80
    order by count(*) DESC;
    """

    print(hash_query(complex_query.upper(), 5))
    print(hash_query(complex_query.title(), 10))
    print(hash_query(complex_query.lower(), 11))
    print(hash_query(complex_query.casefold(), 27))

    shuffled_query = complex_query.split()
    shuffle(shuffled_query)
    print(hash_query(' '.join(shuffled_query)))