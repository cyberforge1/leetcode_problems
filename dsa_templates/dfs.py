### DFS

### SYSTEM STACK TEMPLATE

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []  # List of neighboring nodes

def DFS(cur, target, visited=None):
    """
    Return True if there is a path from cur to target using recursive DFS.
    """
    if cur == target:
        return True

    if visited is None:
        visited = set()

    visited.add(cur)

    for neighbor in cur.neighbors:
        if neighbor not in visited:
            if DFS(neighbor, target, visited):
                return True

    return False


### EXPLICIT STACK TEMPLATE

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []  # List of neighboring nodes

def DFS(root, target):
    """
    Return True if there is a path from root to target using iterative DFS.
    """
    if not root:
        return False

    stack = [root]
    visited = set([root])

    while stack:
        cur = stack.pop()

        if cur == target:
            return True

        for neighbor in cur.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return False



