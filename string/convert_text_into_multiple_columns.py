COL_WIDTH = 20
COL_SEP = "\t\t"


def text_to_columns(text: str):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    columns: [[str]] = []
    max_row = 0
    for line in text.splitlines():
        line = line.strip()
        if line == "":
            continue

        rows: [str] = []
        for word in line.split():
            if len(rows) == 0 or COL_WIDTH < len(rows[-1]) + 1 + len(word):
                rows.append("")
            else:
                rows[-1] += " "
            rows[-1] += word

        columns.append(rows)
        if max_row < len(rows):
            max_row = len(rows)

    result_text: str = ""
    for i in range(max_row):
        for column in columns:
            if i < len(column):
                result_text += column[i]
            result_text += COL_SEP
        result_text = result_text.rstrip()
        result_text += '\n'
    return result_text.rstrip()


if __name__ == '__main__':
    TEXT = """My house is small but cosy.

        It has a white kitchen and an empty fridge.

        I have a very comfortable couch, people love to sit on it.

        My mornings are filled with coffee and reading, if only I had a garden"""

    print(text_to_columns(TEXT))