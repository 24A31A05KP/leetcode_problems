# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        self.sumi=0
        def summ(root,s):
            if root is None:
                return
            if root.left is None and root.right is None:
                self.sumi+=s*10+root.val
                return
            s=s*10+root.val
            summ(root.left,s)
            summ(root.right,s)
        summ(root,0)
        return self.sumi
