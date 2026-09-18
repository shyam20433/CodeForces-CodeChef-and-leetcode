# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen=set()
        def check(root):
            if not root:return False
            diff=k-root.val
            if diff in seen:
                return True
            seen.add(root.val)
            return check(root.left) or check(root.right)
        return check(root)
        """ nums=[]
        def preorder(root):
            if not root:
                return
            nums.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        hash={}
        for i,num in enumerate(nums):
            diff=k-num
            if diff in hash:
                return True
            hash[num]=i
        return False """
        