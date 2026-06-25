"""
Practice: Dataclasses
"""
from dataclasses import dataclass, FrozenInstanceError

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    city: str = "Unknown"

    def __post_init__(self):
        print(f"Person {self.name} created!")

if __name__ == "__main__":
    p = Person("Alice", 30, "NYC")
    print(p)
    try:
        p.age = 31
    except FrozenInstanceError as e:
        print(f"Cannot modify frozen dataclass: {e}")
