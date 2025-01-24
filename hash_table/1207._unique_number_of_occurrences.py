# 1207. Unique Number of Occurrences
# Easy
# Topics
# Companies
# Hint
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:

# Input: arr = [1,2]
# Output: false
# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
 

# Constraints:

# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000



class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        my_dict = {}
        n = len(arr)
        for i in range(n):
            if arr[i] in my_dict:
                my_dict[arr[i]] += 1
            else:
                my_dict[arr[i]] = 1
        values = list(my_dict.values())
        if len(values) == len(set(values)):
            return True
        return False
        
        

# Input: arr = [1,2,2,1,1,3]
# Output: true

# Input: arr = [1,2]
# Output: false

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true     

        
print(Solution().uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]))

# python hash_table/1207._unique_number_of_occurrences.py