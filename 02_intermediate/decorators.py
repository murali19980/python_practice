"""
Practice writing custom decorators for logging, timing, and retry mechanisms.
"""

import time
import functools

def timing_decorator(func):
    # TODO: Implement decorator that measures execution time
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

if __name__ == "__main__":
    print("--- Decorators ---")
