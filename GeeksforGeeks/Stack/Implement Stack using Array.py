class myStack:
    def __init__(self, n):
        # Define Data Structures
        self.stack=[]
        self.n=n
        

    
    def isEmpty(self):
        # Check if stack is empty
        return len(self.stack)==0

    
    def isFull(self):
        # Check if stack is full
        return len(self.stack)==self.n

    
    def push(self, x):
        # Insert x at the top of the stack
        self.stack.append(x)
    
    def pop(self):
        # Removes an element from the top of the stack
        return self.stack.pop() if self.stack else -1

    
    def peek(self):
        return self.stack[-1] if self.stack else -1
        # Returns the top element of the stack