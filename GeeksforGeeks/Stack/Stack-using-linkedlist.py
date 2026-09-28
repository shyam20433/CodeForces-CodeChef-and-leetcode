''' Structure of linked list Node
 class Node:
    def __init__(self, val):
        self.data = val
        self.next = None 
'''

class myStack:

    def __init__(self):
        self.stack=[]
        # Initialize your data members
        

    def isEmpty(self):
        return len(self.stack)==0
        # Check if the stack is empty
        

    def push(self, x):
        self.stack.append(x)
        # Adds element x to the top of the stack
        

    def pop(self):
        return self.stack.pop() if self.stack else -1
        # Removes an element from the top of the stack


    def peek(self):
        return self.stack[-1] if self.stack else -1
        # Returns the top element of the stack
        # If the stack is empty, return -1


    def size(self):
        return len(self.stack)
        # Returns the current size of the stack