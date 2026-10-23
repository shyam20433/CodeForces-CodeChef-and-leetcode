# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        
        def isSame(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            
            return isSame(p.right,q.right) and isSame(p.left,q.left)
        def helper(p,q):
            if not p:
                return False
            if isSame(p,q):
                return True
            return helper(p.right,q) or helper(p.left,q)
        return helper(p,q)

        # approach 2 failed when subRoot have nested children
        # q=deque()
        # q.append(root)
        # outer=[]
        # while q:
        #     inner=[]
        #     node=q.popleft()
        #     inner.append(node.val)
        #     if node.right:
        #         inner.append(node.right.val)
        #         q.append(node.right)
        #     if node.left:
        #         inner.append(node.left.val)
        #         q.append(node.left)
        #     outer.append(inner)
        # print(outer)

        # approach 1 failed 
        # tree1=[]
        # def inorder(root,trees):
        #     if root.left:
        #         inorder(root.left,trees)
        #     trees.append(root.val)
        #     if root.right:
        #         inorder(root.right,trees)
        # inorder(root,tree1)
        # tree2=[]
        # inorder(subRoot,tree2)
        # print(tree1)
        # print(tree2)

        # for i in range(len(tree1)-len(tree2)+1):
        #     sub=tree1[i:i+len(tree2)]
        #     if sub==tree2:
        #         return True
        # return False

        