"""
Practice: Context Managers
Prompt:
1. Create a class-based context manager Timer that prints start time, end time, and elapsed time using __enter__ and __exit__.
2. Create a generator-based context manager open_file(file, mode) using @contextmanager that handles file opening and closing.
3. Test both with a with block.
"""
from contextlib import contextmanager

class Timer:
    # TODO: Implement __enter__ and __exit__
    pass

@contextmanager
def open_file(file, mode):
    # TODO: Implement
    yield

if __name__ == "__main__":
    pass
