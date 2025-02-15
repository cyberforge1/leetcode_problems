# 1. Two Sum
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search(left, right, target):
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == target:
                    return mid
                elif numbers[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        for i in range(len(numbers)):
            complement = target - numbers[i]
            index = binary_search(i + 1, len(numbers) - 1, complement)
            if index != -1:
                return [i + 1, index + 1]
