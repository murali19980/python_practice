"""
Practice: Tree Traversals (BFS, DFS)
"""
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(root):
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return result

def dfs_inorder(root):
    if not root:
        return []
    return dfs_inorder(root.left) + [root.val] + dfs_inorder(root.right)

def dfs_preorder(root):
    if not root:
        return []
    return [root.val] + dfs_preorder(root.left) + dfs_preorder(root.right)

def dfs_postorder(root):
    if not root:
        return []
    return dfs_postorder(root.left) + dfs_postorder(root.right) + [root.val]

if __name__ == "__main__":
    # Build a sample tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("BFS (Level-order):", bfs(root))
    print("DFS In-order:", dfs_inorder(root))
    print("DFS Pre-order:", dfs_preorder(root))
    print("DFS Post-order:", dfs_postorder(root))
