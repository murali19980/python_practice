"""
Practice: Magic Methods
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __len__(self):
        return 2

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        raise IndexError("Index out of range")

    def __iter__(self):
        yield self.x
        yield self.y

    def __gt__(self, other):
        return (self.x**2 + self.y**2) > (other.x**2 + other.y**2)

if __name__ == "__main__":
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    v3 = v1 + v2
    print(v3)
    print(repr(v3))
    print(f"Length: {len(v3)}")
    print(f"v3[0] = {v3[0]}, v3[1] = {v3[1]}")
    print("Iteration:", list(v3))
    print(f"v3 > v1? {v3 > v1}")
