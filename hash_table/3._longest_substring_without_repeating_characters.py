# Longest Substring Without Repeating Characters

# Solution
# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        start = 0
        max_length = 0
        
        for i, char in enumerate(s):
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1
            
            char_map[char] = i
            
            max_length = max(max_length, i - start + 1)
        
        return max_length
        


# Input: s = "abcabcbb"
# Output: 3

# Input: s = "bbbbb"
# Output: 1

# Input: s = "pwwkew"
# Output: 3

        
print(Solution().lengthOfLongestSubstring(s = "pwwkew"))

# python hash_table/3._longest_substring_without_repeating_characters.py