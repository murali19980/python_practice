"""
Practice: NumPy Arrays
"""
import numpy as np

def numpy_demo():
    arr = np.array([1, 2, 3, 4, 5, 6])
    print("Original:", arr)
    reshaped = arr.reshape(2, 3)
    print("Reshaped (2,3):\n", reshaped)
    print("Second row, first two columns:", reshaped[1, :2])

    flattened = arr.flatten()
    print(f"Mean: {np.mean(flattened):.2f}")
    print(f"Median: {np.median(flattened):.2f}")
    print(f"Std Dev: {np.std(flattened):.2f}")

if __name__ == "__main__":
    numpy_demo()
