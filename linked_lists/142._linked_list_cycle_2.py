#   Linked List Cycle II

# Solution
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# Do not modify the linked list.

 

# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
# Example 2:


# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
# Example 3:


# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
 

# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
 

# Follow up: Can you solve it using O(1) (i.e. constant) memory?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        
        if not head or not head.next:
            return None
        
        # Determining if there is a cycle
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else: return None
        
        # Finding the index position of the start of cycle
        
        fast = head
        
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return slow
        
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1

# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0

# Input: head = [1], pos = -1
# Output: no cycle

        
print(Solution().detectCycle())

# python linked_lists/142._linked_list_cycle_2.py