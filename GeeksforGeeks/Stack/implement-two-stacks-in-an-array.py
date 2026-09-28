class TwoStacks:
    def __init__(self):
        # Initialize the top pointers of both stacks
        self.stack1=[]
        self.stack2=[]

    def push1(self, x):
        # Insert the given element at the top of the first stack
        self.stack1.append(x)

    def push2(self, x):
        self.stack2.append(x)
        # Insert the given element at the top of the second stack

    def pop1(self):
        if not self.stack1:
            return -1
        return self.stack1.pop()
        # Remove and return the top element of the first stack
        # Return -1 if the stack is empty

    def pop2(self):
        if not self.stack2:
            return -1
        return self.stack2.pop()
        # Remove and return the top element of the second stack
        # Return -1 if the stack is empty