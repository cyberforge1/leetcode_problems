#   Add Binary

# Solution
# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_sum = 0
        b_sum = 0
        
        for i in range(len(a)):
            a_sum += int(a[len(a) - 1 - i]) * (2**i)
        
        for i in range(len(b)):
            b_sum += int(b[len(b) - 1 - i]) * (2**i)
        
        total_sum = a_sum + b_sum
        
        if total_sum == 0:
            return "0"
        
        result = ''
        while total_sum > 0:
            quotient, remainder = divmod(total_sum, 2)
            result = str(remainder) + result
            total_sum = quotient
        
        return result

        
# Input: a = "11", b = "1"
# Input: a = "1010", b = "1011"
        
        
print(Solution().addBinary(a = "1010", b = "1011"))

# python arrays/67._add_binary.py