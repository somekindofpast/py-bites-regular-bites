NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}


def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    if not isinstance(name, str):
        return NOT_FOUND
    name = name.lower()
    result = NOT_FOUND
    if name in group1:
        result = group1[name]
    if name in group2:
        result = group2[name]
    if name in group3:
        result = group3[name]
    return result


if __name__ == '__main__':
    print(get_person_age("aNA"))
    print(get_person_age("THOmas"))
    print(get_person_age(2))