"""
Practice custom context managers using the contextlib module or __enter__/__exit__ methods.
"""

from contextlib import contextmanager

class CustomOpen:
    # TODO: Implement file-like context manager using classes
    pass

@contextmanager
def custom_context():
    # TODO: Implement context manager using generator and @contextmanager
    yield

if __name__ == "__main__":
    print("--- Context Managers ---")
