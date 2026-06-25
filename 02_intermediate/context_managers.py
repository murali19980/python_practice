"""
Practice: Context Managers
Exercises:
1. Write a custom context manager using __enter__ and __exit__ to time code execution.
2. Write another using the @contextmanager decorator.
"""
from contextlib import contextmanager

class TimerContext:
    # TODO: Implement __enter__ and __exit__
    pass

@contextmanager
def timer_context_decorator():
    # TODO: Implement
    yield

if __name__ == "__main__":
    pass
