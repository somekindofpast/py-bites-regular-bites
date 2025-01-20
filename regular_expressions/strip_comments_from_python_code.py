import re

def strip_comments(code: str):
    code = code.strip()
    started_multiline = False
    stripped_code = ""
    for line in code.splitlines():
        line_stripped = line.strip()
        if re.match(r"^#", line_stripped) is not None:
            continue
        matches = re.findall(r"\"{3}", line_stripped)
        if matches is not None and 0 < len(matches):
            if len(matches) == 1:
                started_multiline = not started_multiline
            continue
        if started_multiline:
            continue
        parts = line.split('#')
        if 1 < len(parts) and re.search(r"'.*#.*'", line) is None:
            line = parts[0]
        stripped_code += line + '\n'
    return stripped_code


if __name__ == "__main__":
    single_comment = '''
    def hello_world():
        # A simple comment preceding a simple print statement
        print("Hello World")
    '''
    print(strip_comments(single_comment))

    single_docstring = '''
    def say_hello(name):
        """A simple function that says hello... Richie style"""
        print(f"Hello {name}, is it me you're looking for?")
    '''
    print(strip_comments(single_docstring))

    class_with_method = '''
    class SimpleClass:
        """Class docstrings go here."""

        def say_hello(self, name: str):
            """Class method docstrings go here."""
            print(f'Hello {name}')
    '''
    print(strip_comments(class_with_method))

    multiline_docstring = '''
    def __init__(self, name, sound, num_legs):
        """
        Parameters
        ----------
        name : str
            The name of the animal
        sound : str
            The sound the animal makes
        num_legs : int, optional
            The number of legs the animal (default is 4)
        """
        self.name = name
        self.sound = sound
        self.num_legs = num_legs
    '''
    print(strip_comments(multiline_docstring))

    code_bite_description = '''
    """this is
    my awesome script
    """
    # importing modules
    import re

    def hello(name):
        """my function docstring"""
        return f'hello {name}'  # my inline comment
    '''
    print(strip_comments(code_bite_description))

    false_positive_after_strip = '''
    def foo():
        print('this is not a #comment')
    '''
    print(strip_comments(false_positive_after_strip))