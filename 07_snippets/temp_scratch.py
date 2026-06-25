"""
DAILY SCRATCHPAD
Date: 2026-06-26
Purpose: Throwaway testing for new ideas.
"""
from datetime import datetime

print(f"Scratchpad: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("-" * 30)

# --- Paste your daily experiments below this line ---

# Example: Walrus operator
if (n := len([1, 2, 3])) > 2:
    print(f"List has {n} elements, more than 2.")

# Example: Zip unpacking
names = ["Alice", "Bob"]
scores = [95, 82]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# --- Clean up or comment out when done ---
