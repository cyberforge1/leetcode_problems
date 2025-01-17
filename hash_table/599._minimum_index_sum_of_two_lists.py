# Minimum Index Sum of Two Lists

# Solution
# Given two arrays of strings list1 and list2, find the common strings with the least index sum.

# A common string is a string that appeared in both list1 and list2.

# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

# Return all the common strings with the least index sum. Return the answer in any order.

 

# Example 1:

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only common string is "Shogun".
# Example 2:

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.
# Example 3:

# Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
# Output: ["sad","happy"]
# Explanation: There are three common strings:
# "happy" with index sum = (0 + 1) = 1.
# "sad" with index sum = (1 + 0) = 1.
# "good" with index sum = (2 + 2) = 4.
# The strings with the least index sum are "sad" and "happy".
 

# Constraints:

# 1 <= list1.length, list2.length <= 1000
# 1 <= list1[i].length, list2[i].length <= 30
# list1[i] and list2[i] consist of spaces ' ' and English letters.
# All the strings of list1 are unique.
# All the strings of list2 are unique.
# There is at least a common string between list1 and list2.



# # Brute Force
# class Solution(object):
#     def findRestaurant(self, list1, list2):
#         """
#         :type list1: List[str]
#         :type list2: List[str]
#         :rtype: List[str]
#         """
#         min_index_sum = float('inf')
#         result = []

#         # Compare each element in list1 with each element in list2
#         for i in range(len(list1)):
#             for j in range(len(list2)):
#                 if list1[i] == list2[j]:
#                     # Calculate index sum
#                     index_sum = i + j
#                     if index_sum < min_index_sum:
#                         # Found a smaller index sum, reset the result list
#                         min_index_sum = index_sum
#                         result = [list1[i]]
#                     elif index_sum == min_index_sum:
#                         # Add to the result list if index sum matches the minimum
#                         result.append(list1[i])
        
#         return result



class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        result = []
        index_sum = float('inf')
        dict1 = {value: index for index, value in enumerate(list1)}
        
        for i in range(len(list1)):
            if list1[i] in dict1 and list1[i] in list2:
                current_sum = i + list2.index(list1[i])
                
                if current_sum < index_sum:
                    # Found a smaller index sum, reset the result list
                    index_sum = current_sum
                    result = [list1[i]]
                elif current_sum == index_sum:
                    # Add to the result list if index sum matches the minimum
                    result.append(list1[i])
                    
        return result






# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]

# Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
# Output: ["sad","happy"]
        
print(Solution().findRestaurant(list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]))

# python hash_table/599._minimum_index_sum_of_two_lists.py