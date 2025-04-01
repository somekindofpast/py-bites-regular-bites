def combine_and_count(a: dict, b: dict) -> dict:
    """Combine two dictionaries.

    Return  new dictionary with the combined keys and values.
    For any key found in both dictionaries,
    return the sum of the values for that key.

    Args:
      a: The first dictionary.
      b: The second dictionary.

    Returns:
      A dictionary with the contents of both.
      Values of any shared keys are summed.
    """
    if not isinstance(a, dict) or not isinstance(b, dict):
        raise TypeError
    for val in a.values():
        if not isinstance(val, int):
            raise TypeError
    for val in b.values():
        if not isinstance(val, int):
            raise TypeError

    comb = a | b
    for key in comb.keys():
        if key in a and key in b:
            comb[key] = a[key] + b[key]
    return comb