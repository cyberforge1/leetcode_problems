# 20. Valid Parentheses
# Easy
# Topics
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.



class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        complements = {'(': ')', '{': '}', '[': ']'}
        
        for char in s:
            if char in complements:
                stack.append(char)
            else:
                if not stack:
                    return False
                stack_top = stack.pop()
                if complements[stack_top] != char:
                    return False

        return not stack  



# Input: s = "()"
# Output: true


# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false

# Input: s = "([])"
# Output: true
        

        
print(Solution().isValid(s = "()"))

# python stack_and_queue/20._valid_parentheses.py