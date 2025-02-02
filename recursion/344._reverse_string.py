# 344. Reverse String
# Solved
# Easy
# Topics
# Companies
# Hint
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105

# s[i] is a printable ascii character.


# ATTEMPT 1

# class Solution(object):
#     def reverseString(self, s):
#         """
#         :type s: List[str]
#         :rtype: None Do not return anything, modify s in-place instead.
#         """
        
#         def helper(left, right):
#             if left >= right:
#                 return   
#             s[left], s[right] = s[right], s[left]
            
#             helper(left + 1, right - 1)
        
#         helper(0, len(s) - 1)     
        
        
        
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        if len(s) == 1 or len(s) == 0:
            return s
        
        left = 0
        right = len(s) - 1
        
        def swap(left, right):
            
            if left >= right:
                return s
            
            s[left], s[right] = s[right], s[left]
                
            swap(left + 1, right - 1)
            
        swap(left, right)
        

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
        
print(Solution().reverseString(s = ["h","e","l","l","o"]))

# python recursion/344._reverse_string.py
        
