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
        
from collections import deque  # Import deque for BFS queue

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:  # Edge case: Empty grid
            return 0

        rows, cols = len(grid), len(grid[0])  # Grid dimensions
        num_islands = 0  # Count of islands
        visited = set()  # Tracks visited land cells
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        def bfs(r, c):
            queue = deque([(r, c)])  # Initialize queue
            visited.add((r, c))  # Mark cell as visited

            while queue:
                x, y = queue.popleft()  # Process current cell
                for dr, dc in directions:
                    nr, nc = x + dr, y + dc  # Compute new position
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        grid[nr][nc] == '1' and (nr, nc) not in visited):
                        queue.append((nr, nc))  # Add new land cell to queue
                        visited.add((nr, nc))  # Mark as visited

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:  # New island found
                    num_islands += 1  # Increment island count
                    bfs(r, c)  # Start BFS from this cell

        return num_islands  # Return total island count




### DFS (Explicit Stack)

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:  # Edge case: Empty grid
            return 0
        
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        visited = set()  # Set to track visited cells
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        def dfs_stack(r, c):
            stack = [(r, c)]  # Initialize stack with starting position
            visited.add((r, c))  # Mark as visited

            while stack:
                x, y = stack.pop()  # Process the current cell
                
                for dr, dc in directions:
                    nr, nc = x + dr, y + dc  # Compute new position
                    
                    # Check if within bounds, is land ('1'), and not visited
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        grid[nr][nc] == '1' and (nr, nc) not in visited):
                        stack.append((nr, nc))  # Push to stack for future processing
                        visited.add((nr, nc))  # Mark as visited

        # Traverse the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:  # Found a new island
                    num_islands += 1  # Increment island count
                    dfs_stack(r, c)  # Start DFS using stack
        
        return num_islands  # Return total island count



        
### DFS (System Stack)


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
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        def dfs(r, c):
            # Boundary check + check if the cell is water ('0') or already visited
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                grid[r][c] == '0' or (r, c) in visited):
                return
            
            # Mark the cell as visited
            visited.add((r, c))

            # Explore all four directions dynamically
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Iterate through the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:  # If land is found and not visited
                    num_islands += 1
                    dfs(r, c)  # Start DFS for this island
        
        return num_islands
