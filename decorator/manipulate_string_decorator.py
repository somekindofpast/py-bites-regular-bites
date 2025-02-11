from functools import wraps


DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            text_array: [str] = list(function(*args, **kwargs))
            if start < end and start < len(text_array):
                start_val = min(max(0, start), len(text_array) - 1)
                end_val = min(max(0, end), len(text_array))
                for i in range(start_val, end_val):
                    text_array[i] = DOT
            return ''.join(text_array)
        return wrapper
    return decorator


if __name__ == '__main__':
    TEXTS = ['Hello world', 'Welcome to PyBites',
             'Decorators for fun and profit',
             'Hello world Hello']

    start = 20
    end = 100

    @strip_range(start, end)
    def gen_output(text):
        return text

    print(gen_output(text=TEXTS[2]))