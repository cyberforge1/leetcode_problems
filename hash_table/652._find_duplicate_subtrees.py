# Find Duplicate Subtrees

# Solution
# Given the root of a binary tree, return all duplicate subtrees.

# For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with the same node values.

 

# Example 1:


# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
# Example 2:


# Input: root = [2,1,1]
# Output: [[1]]
# Example 3:


# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
 

# Constraints:

# The number of the nodes in the tree will be in the range [1, 5000]
# -200 <= Node.val <= 200

# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[Optional[TreeNode]]
        """
        from collections import defaultdict
        
        def serialize(node):
            """Serialize the subtree rooted at 'node'."""
            if not node:
                return "#"
            
            left_serial = serialize(node.left)
            right_serial = serialize(node.right)
            subtree_serial = "{},{},{}".format(node.val, left_serial, right_serial)
            
            # Increment the count of this serialized subtree
            subtree_map[subtree_serial].append(node)
            
            return subtree_serial
        
        subtree_map = defaultdict(list)
        serialize(root)
        
        # Collect root nodes of duplicate subtrees
        return [nodes[0] for nodes in subtree_map.values() if len(nodes) > 1]

    
    
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]

# Input: root = [2,1,1]
# Output: [[1]]
    
    
print(Solution().findDuplicateSubtrees())

# python hash_table/652._find_duplicate_subtrees.py