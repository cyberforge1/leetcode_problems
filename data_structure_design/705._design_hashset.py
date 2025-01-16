# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

# Example 1:

# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]

# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
 

# Constraints:

# 0 <= key <= 106
# At most 104 calls will be made to add, remove, and contains.

class MyHashSet:
    def __init__(self):
        # Create a boolean array with size 10^6 + 1 (to handle keys from 0 to 10^6)
        self.size = 10**6 + 1
        self.data = [False] * self.size

    def add(self, key):
        """
        Inserts the value key into the HashSet.
        :type key: int
        :rtype: None
        """
        self.data[key] = True

    def remove(self, key):
        """
        Removes the value key in the HashSet. If key does not exist, do nothing.
        :type key: int
        :rtype: None
        """
        self.data[key] = False

    def contains(self, key):
        """
        Returns whether the value key exists in the HashSet.
        :type key: int
        :rtype: bool
        """
        return self.data[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)