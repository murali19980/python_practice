"""
Practice: Collections Module
"""
from collections import Counter, defaultdict, deque, namedtuple

def counter_demo():
    text = "mississippi"
    freq = Counter(text)
    print(f"Character frequencies: {freq}")

def defaultdict_demo():
    words = ["apple", "banana", "apricot", "blueberry"]
    grouped = defaultdict(list)
    for w in words:
        grouped[w[0]].append(w)
    print("Grouped by first letter:", dict(grouped))

def deque_demo():
    dq = deque([1, 2, 3])
    dq.appendleft(0)
    dq.append(4)
    print(f"Deque: {dq}")
    print(f"Pop left: {dq.popleft()}")
    print(f"Pop right: {dq.pop()}")

def namedtuple_demo():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    print(f"Namedtuple Point: x={p.x}, y={p.y}")

if __name__ == "__main__":
    counter_demo()
    defaultdict_demo()
    deque_demo()
    namedtuple_demo()
