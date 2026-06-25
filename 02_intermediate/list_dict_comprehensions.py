"""
Practice: List & Dict Comprehensions
"""
def square_evens(numbers):
    return [x**2 for x in numbers if x % 2 == 0]

def flatten_matrix(matrix):
    return [num for row in matrix for num in row]

def invert_dict_comp(d):
    # Using actual dictionary comprehension with aggregation
    return {v: [k for k, val in d.items() if val == v] for v in set(d.values())}

def unique_first_letters(words):
    return {word[0] for word in words if word}

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    print("Squares of evens:", square_evens(nums))
    matrix = [[1, 2, 3], [4, 5, 6]]
    print("Flattened:", flatten_matrix(matrix))
    d = {"a": 1, "b": 2, "c": 1}
    print("Inverted via dict comp:", invert_dict_comp(d))
    words = ["apple", "banana", "apricot", "blueberry"]
    print("Unique first letters:", unique_first_letters(words))
