"""
Practice: itertools
"""
import itertools

def cycle_traffic_light():
    lights = itertools.cycle(['Green', 'Yellow', 'Red'])
    for _ in range(5):
        print(next(lights), end=" ")
    print()

def find_combinations(lst, r=2):
    return list(itertools.combinations(lst, r))

def group_by_odd_even(nums):
    nums_sorted = sorted(nums)
    grouped = itertools.groupby(nums_sorted, key=lambda x: x % 2)
    return {("Even" if key == 0 else "Odd"): list(group) for key, group in grouped}

if __name__ == "__main__":
    print("Traffic light cycle:")
    cycle_traffic_light()
    print("Combinations of [1,2,3,4] r=2:", find_combinations([1,2,3,4]))
    nums = [1, 2, 3, 4, 5, 6]
    print("Grouped even/odd:", group_by_odd_even(nums))
