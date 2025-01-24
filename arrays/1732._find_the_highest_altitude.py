# 1732. Find the Highest Altitude
# Easy
# Topics
# Companies
# Hint
# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

 

# Example 1:

# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
# Example 2:

# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
 

# Constraints:

# n == gain.length
# 1 <= n <= 100
# -100 <= gain[i] <= 100


# FIRST SOLUTION

# class Solution(object):
#     def largestAltitude(self, gain):
#         """
#         :type gain: List[int]
#         :rtype: int
#         """
#         max_altitude = 0
#         current_altitude = 0

#         for g in gain:
#             current_altitude += g
#             max_altitude = max(max_altitude, current_altitude)

#         return max_altitude
        
        
        
        
        
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_sum = 0
        max_alt = 0
        n = len(gain)
        for i in range(n):
            current_sum += gain[i]
            if current_sum > max_alt:
                max_alt = current_sum
        return max_alt        
        
        

# Input: gain = [-5,1,5,0,-7]
# Output: 1

# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
        
        
print(Solution().largestAltitude(gain = [-4,-3,-2,-1,4,3,2]))

# python arrays/1732._find_the_highest_altitude.py