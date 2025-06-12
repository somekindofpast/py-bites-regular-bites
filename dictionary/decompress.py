from typing import Dict


def decompress(string: str, table: Dict[str, str]) -> str:
    if string == "" or table == {}:
        return string
    i = 0
    while True:
        try:
            string = string[:i] + table[string[i]] + (string[i+1:] if i + 1 < len(string) else "")
            i -= 1
        except:
            pass
        if len(string) - 1 <= i:
            break
        i += 1
    return string