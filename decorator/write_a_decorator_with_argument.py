from functools import wraps


def make_html(element):
    def decorator(function):
        @wraps(function)
        def wrapper():
            func = function()
            enclosed_func = f"<{element}>{func}</{element}>"
            return enclosed_func
        return wrapper
    return decorator


if __name__ == '__main__':
    @make_html('p')
    @make_html('strong')
    def get_text(text='I code with PyBites'):
        return text

    print(get_text())