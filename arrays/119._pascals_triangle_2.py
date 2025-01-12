# Pascal's Triangle II

# Solution
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 

# Constraints:

# 0 <= rowIndex <= 33
 

# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        
        for _ in range(rowIndex):
            row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
        
        return row
        
        
        
# Input: rowIndex = 3
# Output: [1,3,3,1]

# Input: rowIndex = 0
# Output: [1]

# Input: rowIndex = 1
# Output: [1,1]
        
print(Solution().getRow(rowIndex = 3))

# python arrays/119._pascals_triangle_2.py