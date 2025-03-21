from typing import Tuple
import re

TEXT = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
VOWELS = 'aeiou'


def strip_vowels(text: str = TEXT) -> Tuple[str, int]:
    """
    Replace all vowels in the input text string by a star
    character (*).
    Return a tuple of (replaced_text, number_of_vowels_found)

    So if this function is called like:
    strip_vowels('hello world')

    ... it would return:
    ('h*ll* w*rld', 3)

    str/int/Tuple in the function definition are type hints, see:
    https://docs.python.org/3/library/typing.html
    and:
    https://pybit.es/articles/code-better-with-type-hints-part-1/
    """
    p = re.compile('[' + VOWELS + ']', re.IGNORECASE)
    return p.subn('*', text)