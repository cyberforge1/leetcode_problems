#   Insert Delete GetRandom O(1)

# Solution
# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

 

# Example 1:

# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]

# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

# Constraints:

# -231 <= val <= 231 - 1
# At most 2 * 105 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is called.


import random

class RandomizedSet:
    def __init__(self):
        """
        Initialize the RandomizedSet object.
        """
        self.num_map = {}  # Hash map to store the value and its index in the list
        self.num_list = []  # List to store values for O(1) random access

    def insert(self, val):
        """
        Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
        :type val: int
        :rtype: bool
        """
        if val in self.num_map:
            return False  # Value already exists in the set
        self.num_list.append(val)  # Add the value to the list
        self.num_map[val] = len(self.num_list) - 1  # Store the index of the value in the list
        return True

    def remove(self, val):
        """
        Removes an item val from the set if present. Returns true if the item was present, false otherwise.
        :type val: int
        :rtype: bool
        """
        if val not in self.num_map:
            return False  # Value does not exist in the set
        # Get the index of the value to remove
        index = self.num_map[val]
        # Swap the last element with the element to remove (to maintain O(1) removal)
        last_val = self.num_list[-1]
        self.num_list[index] = last_val
        self.num_map[last_val] = index
        # Remove the last element from the list and hash map
        self.num_list.pop()
        del self.num_map[val]
        return True

    def getRandom(self):
        """
        Returns a random element from the set.
        :rtype: int
        """
        return random.choice(self.num_list)  # Randomly select an element from the list



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()