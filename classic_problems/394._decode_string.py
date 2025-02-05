# 394. Decode String
# Medium
# Topics
# Companies
# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
 

# Constraints:

# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].

### RECURSIVE SOLUTION (SOLUTION 1)

# class Solution(object):
#     def decodeString(self, s):
#         def helper(index):
#             decoded = ""
#             k = 0

#             while index < len(s):
#                 char = s[index]
#                 if char.isdigit():
#                     k = k * 10 + int(char)
#                 elif char == '[':
#                     index, substring = helper(index + 1)
#                     decoded += k * substring
#                     k = 0
#                 elif char == ']':
#                     return index, decoded
#                 else:
#                     decoded += char
#                 index += 1

#             return index, decoded

#         return helper(0)[1]

class Solution(object):
    def decodeString(s):
        stack = []  # Stack to keep track of previous string and repeat count
        curr_str = ""  # Current string being built
        num = 0  # Number before '[' to determine repetitions

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  # Handles multi-digit numbers
            elif char == "[":
                stack.append((curr_str, num))  # Push the current string and count
                curr_str = ""  # Reset the current string
                num = 0  # Reset the number
            elif char == "]":
                prev_str, repeat_count = stack.pop()  # Pop last string and count
                curr_str = prev_str + (curr_str * repeat_count)  # Decode and append
            else:
                curr_str += char  # Normal character, just append

        return curr_str



# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"


print(Solution().decodeString(s = "3[a]2[bc]"))

# python stack_and_queue/394._decode_string.py