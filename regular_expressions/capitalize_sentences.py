import re

def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""
    text = re.sub(f"([.?!] )(.)", lambda x: f"{x.group(1)}{x.group(2).upper()}", text)
    return text[0].upper() + text[1:]


if __name__ == "__main__":
    print(capitalize_sentences("sentence1? sentence2. sentence3 words! sentence4."))