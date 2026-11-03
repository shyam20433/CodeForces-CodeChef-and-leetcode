# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        res=[]
        def check(root):
            if not root:
                return
            res.append(root.val)
            check(root.left)
            check(root.right)
        check(root)
        return res
        