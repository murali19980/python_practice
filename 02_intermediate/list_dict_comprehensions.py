"""
Practice: List & Dict Comprehensions
Goal: Master concise Python loops.
"""

def main():
    # 1. List Comp: Square of evens from 1 to 20
    squares = [x**2 for x in range(1, 21) if x % 2 == 0]
    print("Even squares:", squares)

    # 2. Nested List Comp: Flatten a matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print("Flattened:", flattened)

    # 3. Dict Comp: Invert a dictionary {name: age} -> {age: [names]}
    names_ages = {"Alice": 30, "Bob": 25, "Charlie": 30}
    inverted = {age: [name for name, a in names_ages.items() if a == age] for age in set(names_ages.values())}
    print("Inverted dict:", inverted)

    # 4. Set Comp: Unique first letters
    words = ["apple", "banana", "apricot", "blueberry"]
    first_letters = {word[0] for word in words}
    print("Unique first letters:", first_letters)

if __name__ == "__main__":
    main()
