"""
Practice: Context Managers
"""
import time
import os
from contextlib import contextmanager

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {elapsed:.4f}s")

@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    try:
        yield f
    finally:
        f.close()

if __name__ == "__main__":
    with Timer():
        time.sleep(0.5)

    filename = "test_ctx.txt"
    with open_file(filename, "w") as f:
        f.write("Hello context manager!")
    print("File written successfully.")

    # Clean up generated file to keep workspace clean
    if os.path.exists(filename):
        os.remove(filename)
