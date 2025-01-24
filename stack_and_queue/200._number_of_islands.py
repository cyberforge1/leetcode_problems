# 200. Number of Islands
# Medium
# Topics
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.


from collections import deque


class Solution(object):
    def numIslands(self, grid):
        """
        Count the number of islands in a 2D grid using BFS with a visited set.
        :param grid: List[List[str]] - 2D grid where '1' represents land and '0' represents water
        :return: int - Number of islands
        """
        def bfs(start):
            queue = deque([start])
            visited.add(start)

            while queue:
                r, c = queue.popleft()
                # Check all 4 neighbors
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        if not grid:
            return 0

        visited = set()
        num_islands = 0

        # Traverse the entire grid
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    num_islands += 1  # New island found
                    bfs((r, c))       # Explore the entire island using BFS

        return num_islands

        
        

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
        
print(Solution().numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

# python stack_and_queue/200._number_of_islands.py