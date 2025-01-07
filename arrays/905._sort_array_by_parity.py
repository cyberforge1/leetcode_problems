# Sort Array By Parity

# Solution
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

 

# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        p1 = n - 1
        p2 = n - 2
        
        for p2 in range(n-1, -1, -1):
            
            print(p2)
            
            if nums[p2] % 2 != 0:
                
                print('This number is odd', nums[p2])
                
                temp = nums[p1]
                
                nums[p1] = nums[p2]
                
                nums[p2] = temp
                
                p1 -= 1
                
            print('This number is even', nums[p1])
        
        print(nums)
        return nums    
            


print(Solution().sortArrayByParity([3,1,2,4]))

# python arrays/905._sort_array_by_parity.py