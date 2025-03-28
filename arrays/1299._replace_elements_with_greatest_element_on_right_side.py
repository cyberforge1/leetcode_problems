# Replace Elements with Greatest Element on Right Side
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

 

# Example 1:

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.
# Example 2:

# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.

# Constraints:

# 1 <= arr.length <= 104
# 1 <= arr[i] <= 105


class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        current_max = -1  # Initialize the max seen so far to -1
        
        for i in range(n - 1, -1, -1):
            temp = arr[i]       # Store the current value
            arr[i] = current_max  # Replace with max seen so far
            current_max = max(current_max, temp)  # Update max seen so far
            
        return arr
           
        
print(Solution().replaceElements([17,18,5,4,6,1]))

# python 1299._replace_elements_with_greatest_element_on_right_side.py