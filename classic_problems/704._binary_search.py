# 704. Binary Search
# Easy
# Topics
# Companies
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.


### ITERATIVE SOLUTION

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Find midpoint
            mid = left + (right - left) // 2
            
            # Return target if found
            if target == nums[mid]:
                return mid
            
            # Search left half
            if target < nums[mid]:
                right = mid - 1
                
            # Search right half
            else:
                left = mid + 1
        
        # Target not found
        return -1
            

### RECURSIVE SOLUTION









# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
        

        
print(Solution().search(nums = [-1,0,3,5,9,12], target = 9))
        
# python binary_search/704._binary_search.py