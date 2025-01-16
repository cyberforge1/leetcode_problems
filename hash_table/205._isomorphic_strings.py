# Isomorphic Strings

# Solution
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "foo", t = "bar"

# Output: false

# Explanation:

# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true

 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.



class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}
        
        for char1, char2 in zip(s, t):
            if char1 in s_to_t and s_to_t[char1] != char2:
                return False
            if char2 in t_to_s and t_to_s[char2] != char1:
                return False
            
            s_to_t[char1] = char2
            t_to_s[char2] = char1
        
        return True
            
            

# Input: s = "egg", t = "add"
# Output: true

# Input: s = "foo", t = "bar"
# Output: false

# Input: s = "paper", t = "title"
# Output: true

# Input: s = "badc", t = "baba"
# Output: true

            
print(Solution().isIsomorphic(s = "badc", t = "baba"))

# python hash_table/205._isomorphic_strings.py