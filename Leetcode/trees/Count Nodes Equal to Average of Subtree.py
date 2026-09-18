# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count=0
        def check(root):
            if not root:
                return 0,0
            
            left,left_sum=check(root.left)
            right,right_sum=check(root.right)
            total=root.val+left_sum+right_sum
            n=1+left+right

            average=total//n
            if average==root.val:
                self.count+=1
            
            return n,total
        check(root)
        return self.count