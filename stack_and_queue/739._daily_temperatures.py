# 739. Daily Temperatures
# Medium
# Topics
# Companies
# Hint
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(temperatures)
        answer = [0] * n
        
        for i in range(n):
            temp = temperatures[i]
            

            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            
            stack.append(i)
        
        return answer
        
        
        
        
        
        

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
        
print(Solution().dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))

# python stack_and_queue/739._daily_temperatures.py