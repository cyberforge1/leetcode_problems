#   First Unique Character in a String

# Solution
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:

# Input: s = "loveleetcode"

# Output: 2

# Example 3:

# Input: s = "aabb"

# Output: -1

 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_dict = {}

        for char in s:
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1

        for index, char in enumerate(s):
            if my_dict[char] == 1:
                return index

        return -1

# Input: s = "leetcode"
# Output: 0

# Input: s = "loveleetcode"
# Output: 2

# Input: s = "aabb"
# Output: -1


        
print(Solution().firstUniqChar(s = "leetcode"))

# python hash_table/387._first_unqiue_character_in_a_string.py