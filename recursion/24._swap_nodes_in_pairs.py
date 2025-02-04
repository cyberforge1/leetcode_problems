# Swap Nodes in Pairs

# Solution
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

# Example 1:

# Input: head = [1,2,3,4]

# Output: [2,1,4,3]

# Explanation:



# Example 2:

# Input: head = []

# Output: []

# Example 3:

# Input: head = [1]

# Output: [1]

# Example 4:

# Input: head = [1,2,3]

# Output: [2,1,3]

 

# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100


# Definition for singly-linked list.
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Base case: if there are fewer than 2 nodes, return the head
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Perform the swap
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Return the new head node (second_node after the swap)
        return second_node

### Swaps pairs from the end of the linked list moving backwards

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        def swap_recursive(node):
            if not node or not node.next:
                return node
            
            first_node = node
            second_node = node.next

            first_node.next = swap_recursive(second_node.next)

            second_node.next = first_node

            return second_node

        return swap_recursive(head)