import re


def count_n_repetitions(text, n=1):
    """
    Counts how often characters are followed by themselves for
    n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    """
    repetitions = 0
    repeating_chars = set(re.findall(r"(.)\1+", text, re.DOTALL))
    #print("repeating chars:", repeating_chars)
    for char in repeating_chars:
        repetition_blocks = re.findall(r"[" + re.escape(char) + "]+", text, re.DOTALL)
        #print(repetition_blocks)
        for block in repetition_blocks:
            n_rep = 0
            if 0 < int((len(block) - 1) / n):
                n_rep = 1 + int((len(block) - 1) - n)
            if 0 < n_rep:
                repetitions += n_rep
    return repetitions


def count_n_reps_or_n_chars_following(text, n=1, char=""):
    """
    Counts how often characters are repeated for n times, or
    followed by char n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    char: Character which also counts if repeated n times
    """
    repetitions = count_n_repetitions(text, n)
    #print("repetitions:", repetitions)
    if char == "":
        return repetitions
    char_follow_blocks = re.findall(r".[" + re.escape(char) + "]+", text, re.DOTALL)
    #print("char_follow_blocks:", char_follow_blocks)
    for block in char_follow_blocks:
        if 2 <= len(block) and block[0] != block[1] and 0 < int((len(block) - 1) / n):
            repetitions += 1
    return repetitions


def check_surrounding_chars(text, surrounding_chars):
    """
    Count the number of times a character is surrounded by
    characters from the surrounding_chars list.

    text: UTF-8 compliant input text
    surrounding_chars: List of characters
    """
    sur_car_num = 0
    if 3 <= len(text):
        for i in range(1, len(text)-1):
            if text[i-1] in surrounding_chars and text[i+1] in surrounding_chars:
                #print(text[i], "is surrounded by", surrounding_chars)
                sur_car_num += 1
    return sur_car_num


if __name__ == '__main__':
    print("count_n_repetitions:", count_n_repetitions("   Spaces are fun", 2))
    print()
    print("count_n_repetitions:", count_n_repetitions("\n\n\nAs are newlines\n\n\n", 2))
    print()
    print("count_n_repetitions:", count_n_repetitions("As \t\t\t are tabs\t\t", 2))
    print()
    print("count_n_repetitions:", count_n_repetitions("Greek: εζεζεζεηηηη", 2))
    print()
    print("count_n_reps_or_n_chars_following:", count_n_reps_or_n_chars_following("zz Don't count double!", 1, "z"))
    print()
    print("count_n_reps_or_n_chars_following:", count_n_reps_or_n_chars_following("????[[[?]]]", 1, "["))
    print()
    print("count_n_reps_or_n_chars_following:", count_n_reps_or_n_chars_following("Hello^there", 1, "^"))
    print()
    print("count_n_reps_or_n_chars_following:", count_n_reps_or_n_chars_following("But bob isn't...\t\t", 2, "\t"))
    print()
    print("check_surrounding_chars:", check_surrounding_chars("\nK\nA\tI\t", ["\n", "\t"]))
    print()
    print("check_surrounding_chars:", check_surrounding_chars("SPECIAL^C^HARS?", ["R", "?", "^"]))