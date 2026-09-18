# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.mini=float('inf')
        self.prev=None
        
        def inorder(root):
            if not root:
                return 0
            
            inorder(root.left)
            if self.prev is not None:
                self.mini=min(self.mini,abs(root.val-self.prev))
            self.prev=root.val
            inorder(root.right)
        inorder(root)
        return self.mini
        