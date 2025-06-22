from typing import List


def split_once(text: str, separators: str = None) -> List[str]:
    if text == "":
        return ['']
    if not separators:
        separators = "\t\n\v\f\r "

    res = []
    while True:
        if text == "":
            break
        for i in range(len(text)):
            char = text[i]
            if char in separators:
                res.append((text[:i]))
                text = text[(i + 1):] if i < len(text) - 1 else ""
                separators = separators.replace(char, '')
                break
            if i == len(text) - 1:
                res.append(text)
                text = ""
    return res


if __name__ == '__main__':
    print(split_once("lorem ipsum, dolor sit - amet, consectetur : adipiscing elit. Praesent vitae orc", ",-:"))
    print(split_once("The quick\tbrown\nfox\vjumps \fover\r the\tlazy\vdog\n"))