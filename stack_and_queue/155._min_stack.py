# 155. Min Stack
# Medium
# Topics
# Companies
# Hint
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
 

# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.


class MinStack:

    def __init__(self):
        self.data = []      # Main stack to store all elements
        self.min_stack = [] # Auxiliary stack to store minimums

    def push(self, val):
        """
        Push an element onto the stack.
        """
        self.data.append(val)
        # Push onto min_stack if it's the new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        Remove the top element from the stack.
        """
        if self.data:
            # If the top of data is also the current minimum, pop from min_stack
            if self.data[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.data.pop()

    def top(self):
        """
        Get the top element of the stack.
        """
        if self.data:
            return self.data[-1]
        return None  # Return None if the stack is empty

    def getMin(self):
        """
        Retrieve the minimum element in the stack.
        """
        if self.min_stack:
            return self.min_stack[-1]
        return None  # Return None if the stack is empty

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()