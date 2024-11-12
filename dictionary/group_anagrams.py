from collections import defaultdict


def group_anagrams(strings: list[str]) -> list[list[str]]:
    """Group anagrams together."""
    group_dict = defaultdict(set)
    for string in strings:
        chars = set()
        for char in string:
            chars.add(char)
        group_dict[frozenset(chars)].add(string)
    return [list(values) for values in group_dict.values()]


if __name__ == "__main__":
    print(group_anagrams(["mace", "eat", "cars", "tea", "arcs", "tan", "acme", "ate", "nat", "came", "bat", "scar"]))