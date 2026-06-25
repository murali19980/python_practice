"""
Practice: Lambda, Map, Filter, Reduce
"""
from functools import reduce

def use_map(nums):
    return list(map(lambda x: x**2, nums))

def use_filter(nums):
    return list(filter(lambda x: x % 2 == 0, nums))

def use_reduce(nums):
    return reduce(lambda a, b: a * b, nums)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print("Map (squares):", use_map(nums))
    print("Filter (evens):", use_filter(nums))
    print("Reduce (product):", use_reduce(nums))
