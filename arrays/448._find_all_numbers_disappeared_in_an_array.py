#   Find All Numbers Disappeared in an Array

# Solution
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
 

# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        all_nums = set(range(1, n + 1))
        nums_set = set(nums)
        return list(all_nums - nums_set)
                
                
        

# Input: nums = [4,3,2,7,8,2,3,1]
# Input: nums = [1,1]

print(Solution().findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))

# python arrays/448._find_all_numbers_disappeared_in_an_array.py