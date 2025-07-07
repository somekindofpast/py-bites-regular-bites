import os
from pathlib import Path


def tail(path: Path, n: int):
    """
    Read the last n lines of the filepath passed in.
    The tests will run this function against a 10 million line file,
    validating its completion within 0.1 seconds.
    """

    res = []
    line = ""
    line_count = 0
    with open(path) as f:
        f.seek(0, os.SEEK_END)
        end = f.tell()

        for index in range(end, -1, -1):
            f.seek(index, os.SEEK_SET)
            c = f.read(1)
            if c == '\n' and line != "":
                line_count += 1
                res.append(line.strip()[::-1])
                line = ""
            else:
                line += c
            if n <= line_count:
                break

    return res[::-1]