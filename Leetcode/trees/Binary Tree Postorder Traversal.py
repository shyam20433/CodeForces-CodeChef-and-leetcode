# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        res=[]
        def check(root):
            if not root:
                return
            check(root.left)
            check(root.right)
            res.append(root.val)
        check(root)
        return res
        