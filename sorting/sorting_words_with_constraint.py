def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    nums = [word for word in words if word[0].isnumeric()]
    not_nums = [word for word in words if not word[0].isnumeric()]
    return sorted(not_nums, key=str.casefold) + (sorted(nums))


if __name__ == '__main__':
    words = ("Andrew Carnegie's 64-room chateau at 2 East 91st "
                 "Street was converted into the Cooper-Hewitt National "
                 "Design Museum of the Smithsonian Institution "
                 "in the 1970's").split()
    print(sort_words_case_insensitively(words))