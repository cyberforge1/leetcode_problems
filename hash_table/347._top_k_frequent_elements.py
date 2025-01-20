# Top K Frequent Elements

# Solution
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Step 1: Count frequencies using a hash map
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # Step 2: Create buckets for grouping elements by frequency
        # The size of the bucket array is len(nums) + 1 because max frequency cannot exceed len(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            bucket[freq].append(num)
        
        # Step 3: Collect top k frequent elements
        result = []
        for freq in range(len(bucket) - 1, 0, -1):  # Start from the highest frequency
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:  # Stop when we've collected k elements
                    return result
        

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Input: nums = [1], k = 1
# Output: [1]
        
print(Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2))

# python hash_table/347._top_k_frequent_elements.py



