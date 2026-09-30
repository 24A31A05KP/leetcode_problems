# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        lh=self.leftheight(root)
        rh=self.rightheight(root)
        if lh==rh:
            return (2**lh)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
    def leftheight(self,node):
        count=0
        while node:
            count+=1
            node=node.left
        return count
    def rightheight(self,node):
        count=0
        while node:
            count+=1
            node=node.right
        return count