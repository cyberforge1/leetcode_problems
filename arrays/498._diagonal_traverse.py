#   Diagonal Traverse

# Solution
# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

# Example 1:


# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# Example 2:

# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# -105 <= mat[i][j] <= 105


class Solution(object):
        
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        diagonals = {}

        # Step 1: Group elements by their diagonal index (i + j)
        for i in range(m):
            for j in range(n):
                diagonal_index = i + j
                if diagonal_index not in diagonals:
                    diagonals[diagonal_index] = []
                diagonals[diagonal_index].append(mat[i][j])

        # Step 2: Traverse each diagonal based on its index
        for k in range(len(diagonals)):
            if k % 2 == 0:
                # Even index: Reverse the diagonal for "up-right" order
                result.extend(reversed(diagonals[k]))
            else:
                # Odd index: Keep the diagonal as-is for "down-left" order
                result.extend(diagonals[k])

        return result
        
        
        
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]

# Input: mat = [[1,2],[3,4]]


print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))

# python arrays/498._diagonal_traverse.py