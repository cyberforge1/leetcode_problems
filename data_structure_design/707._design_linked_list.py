# Design Linked List

# Solution
# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:

# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

# Example 1:

# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]

# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
 

# Constraints:

# 0 <= index, val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.

        
        
class Node:
    """
    Node class represents a single node in the linked list.
    Each node contains a value and a pointer to the next node.
    """
    def __init__(self, val=0, next=None):
        self.val = val  # The value stored in the node
        self.next = next  # Pointer to the next node


class MyLinkedList:
    """
    MyLinkedList is a singly linked list implementation.
    It provides methods to:
    - Get the value at a given index.
    - Add nodes at the head, tail, or a specific index.
    - Delete a node at a specific index.
    """
    def __init__(self):
        """
        Initializes the linked list with an empty head and size 0.
        """
        self.head = None  # Head points to the first node of the list
        self.size = 0  # Keeps track of the size of the list

    def get(self, index: int) -> int:
        """
        Retrieves the value of the node at the given index.
        Returns -1 if the index is invalid.
        """
        if index < 0 or index >= self.size:  # Check if index is out of bounds
            return -1  # Return -1 for invalid index

        current = self.head  # Start from the head of the list
        for _ in range(index):  # Traverse the list to the given index
            current = current.next
        return current.val  # Return the value of the node at the index

    def addAtHead(self, val: int) -> None:
        """
        Adds a node with the given value at the head of the list.
        """
        new_node = Node(val, self.head)  # Create a new node pointing to the current head
        self.head = new_node  # Update the head to the new node
        self.size += 1  # Increment the size of the list

    def addAtTail(self, val: int) -> None:
        """
        Appends a node with the given value at the tail of the list.
        """
        new_node = Node(val)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node  # Set the new node as the head
        else:
            current = self.head  # Start from the head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Update the last node's next to the new node
        self.size += 1  # Increment the size of the list

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Adds a node with the given value before the node at the specified index.
        If index equals the size of the list, the new node is appended at the end.
        If index is greater than the size, the node is not inserted.
        """
        if index < 0 or index > self.size:  # Check if index is out of bounds
            return

        if index == 0:  # If adding at the head
            self.addAtHead(val)  # Reuse addAtHead
        else:
            current = self.head  # Start from the head
            for _ in range(index - 1):  # Traverse to the node before the target index
                current = current.next
            new_node = Node(val, current.next)  # Create a new node pointing to the target node
            current.next = new_node  # Update the previous node's next to the new node
            self.size += 1  # Increment the size of the list

    def deleteAtIndex(self, index: int) -> None:
        """
        Deletes the node at the specified index, if the index is valid.
        """
        if index < 0 or index >= self.size:  # Check if index is out of bounds
            return

        if index == 0:  # If deleting the head
            self.head = self.head.next  # Update the head to the next node
        else:
            current = self.head  # Start from the head
            for _ in range(index - 1):  # Traverse to the node before the target index
                current = current.next
            current.next = current.next.next  # Skip the target node by updating the next pointer
        self.size -= 1  # Decrement the size of the list




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)