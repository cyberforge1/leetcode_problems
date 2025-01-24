# 279. Perfect Squares
# Medium
# Topics
# Companies
# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
 

# Constraints:

# 1 <= n <= 104

from collections import deque


class Solution(object):

    def numSquares(self, n):
        # Generate all perfect squares less than or equal to n
        perfect_squares = []
        i = 1
        while i * i <= n:
            perfect_squares.append(i * i)
            i += 1

        # BFS initialization
        queue = deque([n])  # Start from n
        level = 0  # BFS level (number of perfect squares used)
        visited = set()  # To avoid revisiting numbers

        while queue:
            level += 1
            for _ in range(len(queue)):  # Process all nodes at the current level
                current = queue.popleft()

                for square in perfect_squares:
                    next_num = current - square
                    if next_num == 0:  # Found the solution
                        return level
                    if next_num < 0:  # No need to continue if the number becomes negative
                        break
                    if next_num not in visited:
                        visited.add(next_num)
                        queue.append(next_num)

        return level  # Should never reach here if the input is valid




# Input: n = 12
# Output: 3

# Input: n = 13
# Output: 2
        
        
print(Solution().numSquares(n = 12))

# python stack_and_queue/279._perfect_squares.py