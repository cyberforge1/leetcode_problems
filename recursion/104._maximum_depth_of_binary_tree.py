#   Maximum Depth of Binary Tree

# Solution
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100


# FIRST SOLUTION

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def maxDepth(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: int
#         """
#         if not root:
#             return 0
        
#         left_depth = self.maxDepth(root.left)
#         right_depth = self.maxDepth(root.right)
        
#         return 1 + max(left_depth, right_depth)


# SECOND SOLUTION


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            
            return 1 + max(left_depth, right_depth)

        return dfs(root)