# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        # create a stack that store node in a sorted way
        self.stack=[]
        self.pushLeft(root)
        

    def next(self) -> int:
        node=self.stack.pop()
        #push all the right of the tree to the stack by recursive call 
        if node.right:
            self.pushLeft(node.right)
        return node.val

        

    def hasNext(self) -> bool:
        #check stack is not empty
        return len(self.stack)!=0
        
    
    def pushLeft(self,node)-> list:
        #push root and it left child maintaining higher to lower number
        while node:
            self.stack.append(node)
            node=node.left
    # O(n2logn) not optimal

    # def __init__(self, root: TreeNode | None):
    #     self.stack=[]
    #     self.push(root)
        

    # def next(self) -> int:
    #     return self.stack.pop(0)
        

    # def hasNext(self) -> bool:
    #     return len(self.stack)!=0
    
    # def push(self,root)-> list:
    #     if not root:
    #         return
        
    #     self.stack.append(root.val)
    #     if root.right:
    #         self.push(root.right)
    #     if root.left:
    #         self.push(root.left)
    #     self.stack=sorted(self.stack)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()