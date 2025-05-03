def common_languages(programmers: dict):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    lang_list = list(programmers.values())
    common = set(lang_list[0])
    for i in range(1, len(lang_list)):
        common = common & set(lang_list[i])
    return common


if __name__ == "__main__":
    _programmers = dict(bob=['JS', 'PHP', 'Python', 'Perl', 'Java'],
                tim=['Python', 'Haskell', 'C++', 'JS'],
                sara=['Perl', 'C', 'Java', 'Python', 'JS'],
                paul=['C++', 'JS', 'Python'])
    print(common_languages(_programmers))