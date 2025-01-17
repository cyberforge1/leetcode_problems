# Contains Duplicate II

# Solution
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index_map = {}
        
        for i in range(len(nums)):
            if nums[i] in index_map:
                if i - index_map[nums[i]] <= k:
                    return True
            
            index_map[nums[i]] = i
        
        return False
        
        
        
    # for key, value in d.items():
    #     if value == target_value:
    #         return key
    # return None  # Return None if the value is not found
            
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Input: nums = [1,0,1,1], k = 1
# Output: true

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
        
        
print(Solution().containsNearbyDuplicate(nums = [1,2,3,1], k = 3))

# python hash_table/219._contains_duplicate_2.py