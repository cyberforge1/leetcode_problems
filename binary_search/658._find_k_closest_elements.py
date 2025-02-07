
# Code
# Testcase
# Test Result
# Test Result
# 658. Find K Closest Elements
# Medium
# Topics
# Companies
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3

# Output: [1,2,3,4]

# Example 2:

# Input: arr = [1,1,2,3,4,5], k = 4, x = -1

# Output: [1,1,2,3]

 

# Constraints:

# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr is sorted in ascending order.
# -104 <= arr[i], x <= 104

class Solution:
    def findClosestElements(self, arr, k, x):
        from bisect import bisect_left

        # Find the insertion point using binary search
        left = bisect_left(arr, x)
        left, right = left - 1, left  # Initialize two pointers

        # Expand the two pointers to find k closest elements
        while k > 0:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
            k -= 1

        return arr[left + 1:right]

