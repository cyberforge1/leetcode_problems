# 200. Number of Islands
# Solved
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


### BFS
        
from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = '0'  # Mark as visited
            
            while queue:
                x, y = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = x + dr, y + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        queue.append((nr, nc))
                        grid[nr][nc] = '0'  # Mark as visited

        # Traverse the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # New island found
                    num_islands += 1
                    bfs(r, c)  # Start BFS to mark all connected land cells

        return num_islands


        
### DFS


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        visited = set()  # Stores visited cells

        def dfs(r, c):
            # Boundary check + check if the cell is water ('0') or already visited
            if (
                r < 0 or r >= rows or c < 0 or c >= cols or 
                grid[r][c] == '0' or (r, c) in visited
            ):
                return
            
            # Mark the cell as visited
            visited.add((r, c))

            # Explore all four directions (Up, Down, Left, Right)
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right

        # Iterate through the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:  # If land is found and not visited
                    num_islands += 1
                    dfs(r, c)  # Start DFS for this island
        
        return num_islands

