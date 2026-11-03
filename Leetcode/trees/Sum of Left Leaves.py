# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        queue=deque()
        queue.append((root,False))
        total=0
        while queue:
            root,isLeft=queue.popleft()
            if root and isLeft and (not root.right and not root.left):
                total+=root.val
            if root.left:
                queue.append((root.left,True))
            if root.right:
                queue.append((root.right,False))
        return total