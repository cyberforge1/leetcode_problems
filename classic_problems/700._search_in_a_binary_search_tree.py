# Search in a Binary Search Tree

# Solution
# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

# Example 1:


# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Example 2:


# Input: root = [4,2,7,1,3], val = 5
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 107
# root is a binary search tree.
# 1 <= val <= 107


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution(object):
#     def searchBST(self, root, val):
#         if not root or root.val == val:
#             return root

#         if val < root.val:
#             return self.searchBST(root.left, val)

#         return self.searchBST(root.right, val)



### SECOND SOLUTION

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



### RECURSIVE SOLUTION

class Solution(object):
    def searchBST(self, root, val):
        def search(node):
            if not node:
                return None
            if node.val == val:
                return node
            if val < node.val:
                return search(node.left)
            else:
                return search(node.right)
        
        return search(root)
    
    
### ITERATIVE SOLUTION
    
class Solution(object):
    def searchBST(self, root, val):
        current = root
        
        while current:
            if current.val == val:
                return current
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        
        return None