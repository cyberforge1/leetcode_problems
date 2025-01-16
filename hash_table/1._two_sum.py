#  Two Sum

# Solution
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

# # BRUTE FORCE
# class Solution(object):
#     def twoSum(self, nums, target):
#         n = len(nums)
#         for i in range(n):
#             for j in range(n):
#                 print('This is nums[i]', nums[i])
#                 print('This is nums[j]', nums[j])
#                 if i != j and nums[i] + nums[j] == target:
#                     return [i, j]
#         return False
            
            
# # Two Pointer
    
# class Solution(object):
#     def twoSum(self, nums, target):
#         sorted_nums = sorted((num, idx) for idx, num in enumerate(nums))
#         left = 0
#         right = len(nums) - 1

#         while left < right:
#             current_sum = sorted_nums[left][0] + sorted_nums[right][0]

#             if current_sum == target:
#                 return [sorted_nums[left][1], sorted_nums[right][1]]
#             elif current_sum < target:
#                 left += 1
#             else:
#                 right -= 1

#         return []


# class Solution(object):
#     def twoSum(self, nums, target):
#         my_dict = {value: index for index, value in enumerate(nums)}
        
#         for i in range(len(nums)):
#             my_target = target - nums[i]
#             print(f'This is my target {target} - {nums[i]} = {my_target}')
            
#             if my_target in my_dict and my_dict[my_target] != i:
#                 return [i, my_dict[my_target]]
#         return False


class Solution:
    def twoSum(self, nums, target):
        
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_map:
                return [num_map[complement], i]
            
            num_map[num] = i




# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Input: nums = [3,3], target = 6
# Output: [0,1]


print(Solution().twoSum(nums = [3,2,4], target = 6))

# python hash_table/1._two_sum.py