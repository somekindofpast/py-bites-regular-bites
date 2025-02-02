def split_words_and_quoted_text(text: str):
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 elements only"'

       the resulting list would be:
       ['Should', 'give', '3 elements only']
    """
    in_quotes = False
    quote = ""
    word_array = []
    for word in text.split():
        if '\"' in word:
            if not in_quotes:
                quote += word.lstrip('\"')
            else:
                quote += ' ' + word.rstrip('\"')
                word_array.append(quote)
                quote = ""
            in_quotes = not in_quotes
            continue

        if not in_quotes:
            word_array.append(word)
        else:
            quote += ' ' + word
    return word_array



if __name__ == '__main__':
    print(split_words_and_quoted_text('Should give "3 words only"'))
    print(split_words_and_quoted_text('Our first program was "Hello PyBites"'))
    print(split_words_and_quoted_text('Because "Hello World" is really cliche'))
    print(split_words_and_quoted_text('PyBites is a "A Community that Masters Python through Code Challenges"'))