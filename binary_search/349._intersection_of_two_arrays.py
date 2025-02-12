# 349. Intersection of Two Arrays
# Solved
# Easy
# Topics
# Companies
# Given two integer arrays nums1 and nums2, return an array of their 
# intersection
# . Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

class Solution(object):
    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True  # Target found
            elif arr[mid] < target:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half
        return False  # Target not found

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums2.sort()  # Sort nums2 for binary search
        result = []

        for num in set(nums1):  # Ensure uniqueness
            if self.binary_search(nums2, num):  # Check if num exists in nums2
                result.append(num)

        return result