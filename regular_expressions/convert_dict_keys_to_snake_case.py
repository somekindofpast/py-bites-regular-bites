from typing import Dict, List
import re

def snake_case_keys(data):
    if isinstance(data, Dict):
        new_dict = {}
        for key in data.keys():
            new_data = snake_case_keys(data[key])
            new_key = format_key(key)
            new_dict[new_key] = new_data
        return new_dict
    elif isinstance(data, List):
        new_list = []
        for item in data:
            new_list.append(snake_case_keys(item))
        return new_list
    else:
        return data

def format_key(key: str) -> str:
    key = re.sub(r'([A-Za-z])((?=[A-Z]))', r'\1_', key)
    key = re.sub(r'-', r'_', key)
    key = re.sub(r'[A-Z]', lambda m: m.group(0).lower(), key)
    key = re.sub(r'([a-z])((?=[0-9]))', r'\1_', key)
    return key


if __name__ == '__main__':
    stuff = {
            "darthVader": {
                "firstName22": "Anakin",
                "lastName": "Skywalker",
                "appearance": {
                    "helmetColor": "black",
                    "armorColor": "black",
                    "capeColor": "black",
                },
            }
        }

    print(snake_case_keys(stuff))

