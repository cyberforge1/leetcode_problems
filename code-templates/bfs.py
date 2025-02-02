### BFS

### BASIC IMPLEMENTATION

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def BFS(root, target):
    """
    Return the length of the shortest path between root and target node using BFS.
    """
    if not root:
        return -1

    queue = deque([root])
    step = 0

    # BFS traversal
    while queue:
        size = len(queue)
        for _ in range(size):
            cur = queue.popleft()

            if cur == target:
                return step
            
            # Process all neighbors of the current node
            for neighbor in cur.neighbors:
                queue.append(neighbor)

        step += 1

    return -1


### VISITED SET TEMPLATE

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def BFS(root, target):
    """
    Return the length of the shortest path between root and target node.
    """
    if not root:
        return -1

    queue = deque([root])
    visited = set([root])
    step = 0

    # BFS traversal
    while queue:
        size = len(queue)
        for _ in range(size):
            cur = queue.popleft()
            if cur == target:
                return step
            
            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        
        step += 1

    return -1
