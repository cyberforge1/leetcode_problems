# 2352. Equal Row and Column Pairs
# Medium
# Topics
# Companies
# Hint
# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

# Example 1:


# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]
# Example 2:


# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]



class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Dictionary to count row frequencies
        row_count = {}
        for row in grid:
            row_tuple = tuple(row)
            if row_tuple in row_count:
                row_count[row_tuple] += 1
            else:
                row_count[row_tuple] = 1

        count = 0
        n = len(grid)

        # Compare each column as a tuple with the row frequencies
        for col_idx in range(n):
            column = tuple(grid[row_idx][col_idx] for row_idx in range(n))
            if column in row_count:
                count += row_count[column]

        return count



        

        
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1

# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3



print(Solution().equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]]))

# python hash_table/2352._equal_row_and_column_pairs.py