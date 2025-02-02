# 70. Climbing Stairs
# Easy
# Topics
# Companies
# Hint
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45

# FIRST SOLUTION

# class Solution:
#     def __init__(self):
#         self.memo = {}

#     def climbStairs(self, n):
#         if n in self.memo:
#             return self.memo[n]
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
#         return self.memo[n]



### SECOND SOLUTION

def climbStairs(n):
    my_dict = {}

    def helper(n):
        if n in my_dict:
            return my_dict[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        my_dict[n] = helper(n - 1) + helper(n - 2)
        return my_dict[n]
    
    return helper(n)


### RECURSIVE PATTERN

# climbStairs(5)
#  ├── climbStairs(4)
#  │    ├── climbStairs(3)
#  │    │    ├── climbStairs(2) → 2
#  │    │    ├── climbStairs(1) → 1
#  │    │    → returns (2+1) = 3
#  │    ├── climbStairs(2) → 2 (memoized)
#  │    → returns (3+2) = 5
#  ├── climbStairs(3) → 3 (memoized)
#  → returns (5+3) = 8

