"""
Practice: Iterators & Generators
"""
def fibonacci_gen(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def read_large_file_gen(text):
    for line in text.splitlines():
        yield line

if __name__ == "__main__":
    print("Fibonacci (10 terms):")
    for val in fibonacci_gen(10):
        print(val, end=" ")
    print()

    sample_text = "Line 1\nLine 2\nLine 3"
    print("Simulated file read:")
    for line in read_large_file_gen(sample_text):
        print(f"> {line}")
