"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        def check(root):
            if not root:return
            for child in root.children:
                check(child)
            res.append(root.val)
        check(root)
        return res
        