PYBITES = "pybites"


def convert_pybites_chars(text: str):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    converted_text = ""
    for c in text:
        if c.lower() in PYBITES.lower():
            converted_text += c.lower() if c.isupper() else c.upper()
        else:
            converted_text += c
    return converted_text