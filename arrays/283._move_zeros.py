# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you minimize the total number of operations done?

# PREVIOUS SOLUTION

# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
        
#         n = len(nums)
#         writePointer = 0

#         for readPointer in range(n):
#             if nums[readPointer] != 0:
#                 nums[writePointer] = nums[readPointer]
#                 writePointer += 1

#         for i in range(writePointer, n):
#             nums[i] = 0

#         return nums

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        
        w = 0
        r = 0
        n = len(nums)
        if n == 1:
            return nums
        while r < n:
            if nums[r] != 0:
                nums[w] = nums[r]
                w += 1
            r += 1
        for i in range(w, n):
            nums[i] = 0
        return nums




        
        
print(Solution().moveZeroes([0,1,0,3,12]))

# python arrays/283._move_zeros.py