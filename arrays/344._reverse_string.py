# Reverse String

# Solution
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

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        
        n = len(s)
        r = n - 1
        l = 0
        
        while l < r:
            s[l],s[r] = s[r], s[l]
            l += 1
            r -= 1
            
        return s
        
        
        
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
        
print(Solution().reverseString(s = ["H","a","n","n","a","h"]))

# python arrays/344._reverse_string.py