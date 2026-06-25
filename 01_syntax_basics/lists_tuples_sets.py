"""
Practice: Lists, Tuples, Sets
"""
def list_operations():
    nums = [1, 2, 3, 4]
    print("Original:", nums)
    nums.append(5)
    print("Append 5:", nums)
    nums.insert(0, 0)
    print("Insert 0 at index 0:", nums)
    nums.remove(3)
    print("Remove 3:", nums)
    popped = nums.pop()
    print(f"Pop last ({popped}):", nums)
    # Slicing the original nums (1, 2, 3, 4) to get [2, 3]
    original_nums = [1, 2, 3, 4]
    sliced = original_nums[1:3]
    print(f"Slice of original [1:3] to get [2, 3]: {sliced}")
    return nums

def set_operations():
    A = {1, 2, 3}
    B = {3, 4, 5}
    print(f"A: {A}, B: {B}")
    print(f"Union: {A | B}")
    print(f"Intersection: {A & B}")
    print(f"Difference A - B: {A - B}")
    print(f"Symmetric difference: {A ^ B}")

def tuple_example():
    t = (10, 20, 30)
    print(f"Tuple: {t}")
    try:
        t[0] = 100
    except TypeError as e:
        print(f"Modification failed (as expected): {e}")
    lst = list(t)
    lst[0] = 100
    t2 = tuple(lst)
    print(f"Converted to list, modified, back to tuple: {t2}")

if __name__ == "__main__":
    list_operations()
    set_operations()
    tuple_example()
