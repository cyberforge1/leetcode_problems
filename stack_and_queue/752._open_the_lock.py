# 752. Open the Lock
# Medium
# Topics
# Companies
# Hint
# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

# The lock initially starts at '0000', a string representing the state of the 4 wheels.

# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 

# Example 1:

# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation: 
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".
# Example 2:

# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
# Example 3:

# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# Output: -1
# Explanation: We cannot reach the target without getting stuck.

from collections import deque


class Solution(object):

    def openLock(self, deadends, target):
        """
        Solves the "Open the Lock" problem using BFS to find the shortest path
        from the initial state "0000" to the target state, avoiding deadends.
        """
        # Convert deadends to a set for quick lookup
        dead_set = set(deadends)
        start = "0000"

        # If the starting point is in the deadends, return -1 immediately
        if start in dead_set:
            return -1

        # BFS queue: (current lock state, number of moves)
        queue = deque([(start, 0)])
        # Visited set to avoid revisiting states
        visited = {start}

        while queue:
            # Dequeue the current state and number of moves
            current, moves = queue.popleft()

            # If we reached the target, return the number of moves
            if current == target:
                return moves

            # Generate all neighbors of the current state
            for i in range(4):  # Iterate over each of the 4 wheels
                digit = int(current[i])  # Extract the digit at the current wheel
                for change in [-1, 1]:  # Simulate turning the wheel backward or forward
                    # Calculate the new digit with wrap-around
                    new_digit = (digit + change) % 10
                    # Create the new lock state by replacing the current digit
                    new_state = current[:i] + str(new_digit) + current[i+1:]

                    # If the new state is valid, add it to the queue
                    if new_state not in visited and new_state not in dead_set:
                        queue.append((new_state, moves + 1))  # Increment the move count
                        visited.add(new_state)  # Mark the state as visited

        # If the queue is exhausted and the target wasn't found, return -1
        return -1

        
        
        

# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6

# Input: deadends = ["8888"], target = "0009"
# Output: 1

# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# Output: -1
        
print(Solution().openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))

# python stack_and_queue/752._open_the_lock.py