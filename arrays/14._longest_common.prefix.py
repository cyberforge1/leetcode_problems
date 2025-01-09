#   Longest Common Prefix

# Solution
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        prefix = strs[0]
        for string in strs[1:]:
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
            
        
        
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
        
print(Solution().longestCommonPrefix(strs = ["flower","flow","flight"]))

# python arrays/longest_common.prefix.py