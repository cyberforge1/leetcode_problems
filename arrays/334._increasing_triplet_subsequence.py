# 334. Increasing Triplet Subsequence
# Medium
# Topics
# Companies
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

# Constraints:

# 1 <= nums.length <= 5 * 105
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

# Seen this question in a real interview before?
# 1/5


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = j = k = None  # Initialize i, j, k to None (no values assigned yet)

        for idx, num in enumerate(nums):
            if i is None or num <= nums[i]:  # Update i (smallest element index)
                i = idx
            elif j is None or num <= nums[j]:  # Update j (second smallest element index)
                j = idx
            elif k is None or num > nums[j]:  # Found k (greater than both i and j)
                k = idx
                return True  # If i < j < k is valid, return True
        
        return False
        
        
        

# Input: nums = [1,2,3,4,5]
# Output: true

# Input: nums = [5,4,3,2,1]
# Output: false

# Input: nums = [2,1,5,0,4,6]
# Output: true



        
print(Solution().increasingTriplet(nums = [2,1,5,0,4,6]))

# python arrays/334._increasing_triplet_subsequence.py