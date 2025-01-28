# 494. Target Sum
# Medium
# Topics
# Companies
# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

 

# Example 1:

# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# Example 2:

# Input: nums = [1], target = 1
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000


class Solution(object):
    def findTargetSumWays(self, nums, target):
        memo = {}

        def dfs(index, current_sum):
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]

            if index == len(nums):
                return 1 if current_sum == target else 0

            add = dfs(index + 1, current_sum + nums[index])
            subtract = dfs(index + 1, current_sum - nums[index])

            memo[(index, current_sum)] = add + subtract
            return memo[(index, current_sum)]

        return dfs(0, 0)



# Example Usage
# nums = [25,14,16,44,9,22,15,27,23,10,41,25,14,35,28,47,39,26,11,38]
# target = 43
# print(findTargetSumWays(nums, target))
        
        
        
        