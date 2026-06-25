"""
Practice: Arrays & Strings (Sliding Window)
"""
def longest_subarray_sum_k(arr, k):
    left = 0
    curr_sum = 0
    max_len = 0
    for right in range(len(arr)):
        curr_sum += arr[right]
        while curr_sum > k and left <= right:
            curr_sum -= arr[left]
            left += 1
        if curr_sum == k:
            max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 9
    # Subarrays summing to 9: [2,3,4] (len 3), [4,5] (len 2) -> max len = 3
    print(f"Longest subarray length sum {k}: {longest_subarray_sum_k(arr, k)}")
