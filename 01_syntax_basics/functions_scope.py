"""
Practice: Functions & Scope
"""
counter = 0  # global

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def increment():
    global counter
    counter += 1
    return counter

def local_example():
    counter = 10  # local
    print(f"Local counter: {counter}")

if __name__ == "__main__":
    print(greet("Murali"))
    print(greet("Murali", "Hi"))
    print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")
    print_info(name="Alice", age=30, city="NYC")
    print(f"Global counter before increment: {counter}")
    increment()
    print(f"Global counter after increment: {counter}")
    local_example()
    print(f"Global counter remains: {counter}")
