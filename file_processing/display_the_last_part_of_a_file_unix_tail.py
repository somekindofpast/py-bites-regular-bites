from pathlib import Path
from typing import List
import os

def tail(filepath: Path, n: int) -> List[str]:
    """
    Similate Unix' "tail -n" command:
    - Read in the file ("filepath").
    - Parse it into a list of lines, stripping trailing newlines.
    - Return the last "n" lines.
    """
    with open(filepath) as f:
        content = f.read()
    return [line.strip() for line in content.splitlines()][-n:]


if __name__ == '__main__':
    text = """Hello world!
    We hope that you are learning a lot of Python.
    Have fun with our Bites of Py.
    Keep calm and code in Python!
    Become a PyBites ninja!"""

    tmp = os.getenv("TMP", "/tmp")
    path = os.path.join(tmp, 'hello text.txt')
    with open(path, 'w') as f:
        f.write(text)

    print(tail(Path(path), 10))