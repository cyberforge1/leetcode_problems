# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        counter = 0
        consecutive_ones = 0
        for i in nums:
            if i == 1:
                counter += 1
                consecutive_ones = max(consecutive_ones, counter)
            else:
                counter = 0
        return consecutive_ones
            


print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))


# python max_consecutive_ones.py 
