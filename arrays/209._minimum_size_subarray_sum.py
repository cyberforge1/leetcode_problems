#   Minimum Size Subarray Sum

# Solution
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).


class Solution:
    def minSubArrayLen(self, target, nums):
        start = 0
        current_sum = 0
        min_length = float('inf')
        
        for end in range(len(nums)):
            current_sum += nums[end]
            
            while current_sum >= target:
                min_length = min(min_length, end - start + 1)
                current_sum -= nums[start]
                start += 1
        
        return min_length if min_length != float('inf') else 0
        
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2

# Input: target = 4, nums = [1,4,4]
# Output: 1

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
        
print(Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))   

# python arrays/209._minimum_size_subarray_sum.py
