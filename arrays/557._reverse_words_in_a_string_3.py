#   Reverse Words in a String III

# Solution
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "Mr Ding"
# Output: "rM gniD"
 

# Constraints:

# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        split_arr = s.split()
        for i in range(len(split_arr)):
            split_arr[i] = split_arr[i][::-1]
        ans = " ".join(split_arr)
        return ans
        
        
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Input: s = "Mr Ding"
# Output: "rM gniD"
        
        
print(Solution().reverseWords("Let's take LeetCode contest"))


# python arrays/557._reverse_words_in_a_string_3.py