# Reverse Words in a String

# Solution
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Constraints:

# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
 

# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

# PREVIOUS ATTEMPT

# class Solution(object):
#     def reverseWords(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         str_ans = ''
#         L = s.split()
#         L.reverse()
#         for word in L:
#             str_ans += word + ' '
#         return str_ans[0:-1]
        
        
        
        
        
        
        
        
        
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        
        my_arr = s.split()
        i = 0
        j = len(my_arr) - 1

        while i < j:
            my_arr[i], my_arr[j] = my_arr[j], my_arr[i]
            i += 1
            j -= 1
        result = ' '.join(my_arr)
        return result
        

        
        
        
        
        
        
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Input: s = "  hello world  "
# Output: "world hello"

# Input: s = "a good   example"
# Output: "example good a"

        
        
print(Solution().reverseWords(s = "  hello world  "))

# python arrays/151._reverse_words_in_a_string.py