from functools import cache

@cache
def cached_fib(n):
    if n < 2:
        return n
    return cached_fib(n - 2) + cached_fib(n - 1)