# Intersection of Two Arrays II

# Solution
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
 

# Follow up:

# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        
        # Count occurrences of elements in nums1
        my_dict = {}
        for num in nums1:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        
        # Find the intersection with nums2
        for num in nums2:
            if num in my_dict and my_dict[num] > 0:
                result.append(num)
                my_dict[num] -= 1
        
        return result

        
        

        
        

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
        
print(Solution().intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))

# python hash_table/350._intersection_of_two_arrays_2.py