# Jewels and Stones

# Solution
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:

# Input: jewels = "z", stones = "ZZ"
# Output: 0
 

# Constraints:

# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        sum = 0
        my_dict = {}
        
        for char in stones:
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
                        
        for char in jewels:
            if char in my_dict:
                sum += my_dict[char]
                
        return sum 
        
        
        
        
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# Input: jewels = "z", stones = "ZZ"
# Output: 0
        
print(Solution().numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))

# python hash_table/771._jewels_and_stones.py