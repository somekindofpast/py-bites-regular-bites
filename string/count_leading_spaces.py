def count_indents(text: str) -> int:
    """
    Count and return the number of leading white space characters (' ').
    """
    count = 0
    for char in text:
        if char != ' ':
            break
        count += 1
    return count


if __name__ == '__main__':
    print(count_indents('            string'))