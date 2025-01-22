# 643. Maximum Average Subarray I
# Easy
# Topics
# Companies
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 

# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104

class Solution:
    def findMaxAverage(self, nums, k):
        current_window_sum = sum(nums[:k])
        max_window_sum = current_window_sum
        
        for i in range(k, len(nums)):
            current_window_sum += nums[i] - nums[i - k]
            
            max_window_sum = max(max_window_sum, current_window_sum)
        
        return max_window_sum / float(k)
    
    

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000

# Input: nums = [5], k = 1
# Output: 5.00000
    
print(Solution().findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))

# python arrays/643._maximum_average_subarray_I.py