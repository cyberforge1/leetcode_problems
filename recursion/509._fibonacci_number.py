# Fibonacci Number

# Solution
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:

# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

# Constraints:

# 0 <= n <= 30

# BASIC SOLUTION

# class Solution(object):
#     def fib(self, n):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return self.fib(n - 1) + self.fib(n - 2)
        


# MEMOIZATION

# class Solution(object):
#     def __init__(self):
#         self.memo = {}

#     def fib(self, n):
#         if n in self.memo:
#             return self.memo[n]

#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1

#         self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
#         return self.memo[n]


class Solution(object):
    def fib(self, n):
        
        my_dict = {}
        
        def helper(n):
            if n in my_dict:
                return my_dict[n]
            if n == 0 or n == 1:
                my_dict[n] = n
            else:
                my_dict[n] = helper(n-1) + helper(n-2)
                
            return my_dict[n]
        
        return helper(n)
           
        
