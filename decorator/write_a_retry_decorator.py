from functools import wraps

MAX_RETRIES = 3


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""
    # ... retry MAX_RETRIES times
    # ...
    # make sure you include this for testing:
    # except Exception as exc:
    #     print(exc)
    # ...
    # and use wraps to preserve docstring
    #
    @wraps(func)
    def wrapper(numbers):
        retries = 0
        result = None
        while True:
            try:
                result = func(numbers)
            except Exception as exc:
                print(exc)
                retries += 1
            finally:
                if result or retries == MAX_RETRIES:
                    break
        if retries == MAX_RETRIES:
            raise MaxRetriesException
        return result
    return wrapper