# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

# Example 1:

# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
# Example 2:

# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]
 

# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 9

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        n = len(arr)
        
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                print('This item is 0', arr[i])
                print('This is the index position', i)
                print('This is the array segment', arr[i:])
                shifted_segement = arr[i+1:] = arr[i:-1]
                print('This is the shifted segment', shifted_segement)

                
                
                
                
                
            i += 1
        
        
        
        
print(Solution().duplicateZeros([1,0,2,3,0,4,5,0]))

# python duplicate_zeros.py



