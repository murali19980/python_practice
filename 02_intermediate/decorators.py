"""
Practice: Decorators
Goal: Write reusable wrappers for functions.
"""
import time
from functools import wraps

# 1. Timer Decorator
def timer(func):
    @wraps(func)  # Preserves original function name/metadata
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

# 2. Retry Decorator (retries 3 times on failure)
def retry(max_tries=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_tries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt+1} failed: {e}")
            raise RuntimeError(f"All {max_tries} attempts failed.")
        return wrapper
    return decorator

# 3. Cache Decorator (Memoization)
def cache(func):
    store = {}
    @wraps(func)
    def wrapper(*args):
        if args in store:
            print("Returning cached result")
            return store[args]
        result = func(*args)
        store[args] = result
        return result
    return wrapper

# --- Usage ---
@timer
def slow_function():
    time.sleep(1)
    return "Done"

@cache
def expensive_multiply(a, b):
    print("Computing...")
    return a * b

if __name__ == "__main__":
    slow_function()
    expensive_multiply(5, 6)
    expensive_multiply(5, 6)  # This will hit the cache
