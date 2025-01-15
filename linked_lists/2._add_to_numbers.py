#  Add Two Numbers

# Solution
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        arr1 = []
        arr2 = []
        
        
        while l1 or l2:
            if l1:
                arr1.append(l1.val)
                l1 = l1.next
            if l2:
                arr2.append(l2.val)
                l2 = l2.next
                
        int_l1 = int("".join(map(str, reversed(arr1))))
        int_l2 = int("".join(map(str, reversed(arr2))))
        
        sum = int_l1 + int_l2
        
        sum_arr = [int(digit) for digit in str(sum)]
        
        head = None
        
        for digit in reversed(sum_arr):
            new_node = ListNode(digit)
            new_node.next = head
            head = new_node
        return head
            