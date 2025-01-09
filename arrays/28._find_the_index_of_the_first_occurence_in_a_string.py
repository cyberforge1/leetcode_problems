# Implement strStr()

# Solution
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        n = len(needle)

        for i in range(len(haystack) - n + 1):
            if haystack[i:i + n] == needle:
                print('Match found!')
                return i
        
        return -1
        
        
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
        
print(Solution().strStr(haystack = "leetcode", needle = "leeto"))

# python arrays/28._find_the_index_of_the_first_occurence_in_a_string.py