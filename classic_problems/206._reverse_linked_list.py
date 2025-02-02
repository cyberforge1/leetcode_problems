# 206. Reverse Linked List
# Solved
# Easy
# Topics
# Companies
# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


### BUILDS A SEPARATE LINKED LIST (UN-ATTACHED)

### ITERATIVE SOLUTION POINTS CURR.NEXT TO PREV FOR REVERSAL

### PREV IS THE HEAD OF THE NEWLY BUILT LINKED LIST




### ITERATIVE

# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         prev = None
#         curr = head
        
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
            
#         return prev
    
    
### RECURSIVE


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        curr = head
        prev = None
        
        def helper(curr, prev):
            
            if not curr:
                return prev
            
            temp = curr.next
            curr.next = prev
            
            return helper(curr = temp, prev = curr)
            
        return helper(curr, prev)
            
            
            
            