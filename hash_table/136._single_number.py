# Single Number

# Solution
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]

# Output: 1

 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_set = set()
        
        for num in nums:
            if num in my_set:
                my_set.remove(num)
            else:
                my_set.add(num)
        
        return my_set.pop()
        
        
# Input: nums = [2,2,1]
# Output: 1

# Input: nums = [4,1,2,1,2]
# Output: 4

# Input: nums = [1]
# Output: 1
        
        
print(Solution().singleNumber(nums = [2,2,1]))

# python hash_table/136._single_number.py