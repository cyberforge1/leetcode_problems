#   Design Circular Queue

# Solution
# Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

# Implement the MyCircularQueue class:

# MyCircularQueue(k) Initializes the object with the size of the queue to be k.
# int Front() Gets the front item from the queue. If the queue is empty, return -1.
# int Rear() Gets the last item from the queue. If the queue is empty, return -1.
# boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
# boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
# boolean isEmpty() Checks whether the circular queue is empty or not.
# boolean isFull() Checks whether the circular queue is full or not.
# You must solve the problem without using the built-in queue data structure in your programming language. 



# Example 1:

# Input
# ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 3, true, true, true, 4]

# Explanation
# MyCircularQueue myCircularQueue = new MyCircularQueue(3);
# myCircularQueue.enQueue(1); // return True
# myCircularQueue.enQueue(2); // return True
# myCircularQueue.enQueue(3); // return True
# myCircularQueue.enQueue(4); // return False
# myCircularQueue.Rear();     // return 3
# myCircularQueue.isFull();   // return True
# myCircularQueue.deQueue();  // return True
# myCircularQueue.enQueue(4); // return True
# myCircularQueue.Rear();     // return 4
 

# Constraints:

# 1 <= k <= 1000
# 0 <= value <= 1000
# At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.


class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize the circular queue with a fixed size k.
        :type k: int
        """
        self.size = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.head == -1:
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self):
        """
        Check whether the circular queue is empty.
        :rtype: bool
        """
        return self.head == -1

    def isFull(self):
        """
        Check whether the circular queue is full.
        :rtype: bool
        """
        return (self.tail + 1) % self.size == self.head


# python stack_and_queue/622._design_circular_queue.py