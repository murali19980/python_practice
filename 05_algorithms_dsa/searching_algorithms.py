"""
Practice: Searching Algorithms
"""
def binary_search_iter(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_rec(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_rec(arr, target, mid+1, high)
    else:
        return binary_search_rec(arr, target, low, mid-1)

def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        curr = arr[left] + arr[right]
        if curr == target:
            return [left, right]
        elif curr < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    print("Index of 7 (iter):", binary_search_iter(arr, 7))
    print("Index of 7 (rec):", binary_search_rec(arr, 7, 0, len(arr)-1))
    print("Two sum for 12:", two_sum_sorted(arr, 12))
