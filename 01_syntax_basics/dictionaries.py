"""
Practice: Dictionaries
"""
def merge_dicts(d1, d2):
    return {**d1, **d2}

def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        inverted.setdefault(value, []).append(key)
    return inverted

def safe_get(d, key):
    return d.get(key, "Key not found")

def loop_dict():
    d = {"Alice": 25, "Bob": 30}
    for name, age in d.items():
        print(f"{name} is {age} years old")

if __name__ == "__main__":
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    print("Merged:", merge_dicts(d1, d2))

    d = {"a": 1, "b": 2, "c": 1}
    print("Inverted:", invert_dict(d))

    print("Safe get for 'x':", safe_get(d, "x"))
    loop_dict()
