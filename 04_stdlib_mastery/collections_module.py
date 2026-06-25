"""
Practice: Collections Module
Goal: Use Counter, defaultdict, deque efficiently.
"""
from collections import Counter, defaultdict, deque

def main():
    # 1. Counter: Count word frequencies
    text = "apple banana apple orange banana apple"
    word_counts = Counter(text.split())
    print("Most common:", word_counts.most_common(2))  # [('apple', 3), ('banana', 2)]

    # 2. defaultdict: Group items without KeyError
    grouped = defaultdict(list)
    for fruit, count in word_counts.items():
        grouped[count].append(fruit)
    print("Grouped by count:", dict(grouped))

    # 3. deque: Fast appends/pops from both ends
    dq = deque([1, 2, 3])
    dq.appendleft(0)
    dq.append(4)
    print("Deque:", dq)
    print("Popped right:", dq.pop())
    print("Popped left:", dq.popleft())

    # 4. namedtuple (Optional extra: lightweight class)
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    print(f"Point x={p.x}, y={p.y}")

if __name__ == "__main__":
    main()
