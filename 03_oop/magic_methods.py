"""
Practice: Magic Methods (Dunder methods)
Goal: Make custom objects behave like built-in types.
"""
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # String representation
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Addition: v1 + v2
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    # Length: len(v)
    def __len__(self):
        return 2  # Vectors always have 2 components

    # Item access: v[0] or v[1]
    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        raise IndexError("Vector index out of range")

    # Iteration: for val in v
    def __iter__(self):
        yield self.x
        yield self.y

    # Greater than (for sorting)
    def __gt__(self, other):
        return (self.x**2 + self.y**2) > (other.x**2 + other.y**2)

if __name__ == "__main__":
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    v3 = v1 + v2
    print(v3)           # Calls __str__: (4, 6)
    print(repr(v3))     # Calls __repr__: Vector(4, 6)
    print(len(v3))      # Calls __len__: 2
    print(v3[0])        # Calls __getitem__: 4
    for i in v1:        # Calls __iter__
        print(i)        # Prints 3, 4
    print(v3 > v1)      # Calls __gt__: True
