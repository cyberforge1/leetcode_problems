# 733. Flood Fill
# Easy
# Topics
# Companies
# Hint
# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:

# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.

 

# Example 1:

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

# Output: [[2,2,2],[2,2,0],[2,0,1]]

# Explanation:



# From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

# Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

# Example 2:

# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

# Output: [[0,0,0],[0,0,0]]

# Explanation:

# The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.


class Solution(object):

    def floodFill(image, sr, sc, color):
        # Get the initial color of the starting pixel
        initial_color = image[sr][sc]
        
        # Edge case: If the new color is the same as the initial color, return the image
        if initial_color == color:
            return image

        # Helper function to perform DFS
        def dfs(row, col):
            # Base case: Check bounds and if the pixel matches the initial color
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != initial_color:
                return
            
            # Update the color of the current pixel
            image[row][col] = color
            
            # Recur for all 4 directions
            dfs(row - 1, col)  # Up
            dfs(row + 1, col)  # Down
            dfs(row, col - 1)  # Left
            dfs(row, col + 1)  # Right
        
        # Start the DFS from the given starting point
        dfs(sr, sc)
        
        # Return the modified image
        return image
        
