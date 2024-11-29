import string

alphabet_list = [c for c in string.ascii_lowercase]

def convert_string_to_index(input_value: str | list[str]) -> list[int]:
    if not input_value:
        return []
    input_list = []
    results = []
    if isinstance(input_value, str):
        input_list = input_value.split(',')
    else:
        input_list = input_value

    for input_element in input_list:
        ranges = input_element.split(':')
        if len(ranges) == 1:
            results.append(get_character_index(ranges[0]))
        else:
            results.extend(range(get_character_index(ranges[0]), get_character_index(ranges[1]) + 1))

    return results


def get_character_index(input_value: str) -> int:
    input_value = input_value.strip()
    result = 0

    for character in input_value.lower():
        character = character.strip()
        if not character:
            continue
        result += alphabet_list.index(character)
    return result + 26 if 1 < len(input_value) else result


if __name__ == '__main__':
    print(convert_string_to_index("A"))
    print(convert_string_to_index(["A", "B", "Z"]))
    print(convert_string_to_index(["A", "B:C", "D"]))
    print(convert_string_to_index(" A , B : C , D "))
    print(convert_string_to_index("AA, AB, AC"))
    print(convert_string_to_index("AA:AC"))
    print(convert_string_to_index(""))
    print(convert_string_to_index([]))