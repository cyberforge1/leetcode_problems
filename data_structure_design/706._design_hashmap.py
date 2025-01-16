# Design HashMap

# Solution
# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

# Example 1:

# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

# Constraints:

# 0 <= key, value <= 106
# At most 104 calls will be made to put, get, and remove.


class MyHashMap:
    def __init__(self):
        """
        Initialize the data structure. Use a list of buckets where each bucket is a list of key-value pairs.
        """
        self.size = 1000  # Use a smaller size for the primary array to handle collisions with chaining
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        """
        Hash function to compute the index for a given key.
        """
        return key % self.size

    def put(self, key, value):
        """
        Insert a (key, value) pair into the HashMap. If the key already exists, update its value.
        :type key: int
        :type value: int
        :rtype: None
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def get(self, key):
        """
        Get the value associated with the key. Return -1 if the key is not found.
        :type key: int
        :rtype: int
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key):
        """
        Remove the key and its corresponding value if it exists in the HashMap.
        :type key: int
        :rtype: None
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair[0] == key:
                bucket.remove(pair)
                return

# Example usage:
obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))  # Output: 1
print(obj.get(3))  # Output: -1
obj.put(2, 1)
print(obj.get(2))  # Output: 1
obj.remove(2)
print(obj.get(2))  # Output: -1



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# python hash_table/706._design_hashmap.py