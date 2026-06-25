"""
Practice: Graph Algorithms (BFS, DFS)
"""
from collections import deque

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, []).append(u)  # undirected

    def bfs(self, start):
        visited = set()
        result = []
        q = deque([start])
        visited.add(start)
        while q:
            node = q.popleft()
            result.append(node)
            for neighbor in self.adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return result

    def dfs(self, start):
        visited = set()
        result = []
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.adj.get(node, []):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    print("BFS from 0:", g.bfs(0))
    print("DFS from 0:", g.dfs(0))
