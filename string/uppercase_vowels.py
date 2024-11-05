VOWELS = "aeiou"
EXTENSIONS = [".mp3", ".jpg", ".jpeg", ".pdf", ".txt", ".mp4", ".png", ".exe"]


def uppercase_vowels(text: str) -> str:
    result = ""
    for i in range(len(text)):
        if text[i] == '.' and text[i:] in EXTENSIONS:
            result += text[i:]
            break
        elif text[i].isalpha():
            if text[i].lower() in VOWELS:
                result += text[i].upper()
            else:
                result += text[i].lower()
        else:
            result += ' '
    return result


if __name__ == '__main__':
    print(uppercase_vowels("data.jpg foul"))
    print(uppercase_vowels("-,.?~a"))
    print(uppercase_vowels("what is file.pdf"))