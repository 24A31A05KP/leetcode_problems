# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node):
        if node is None:
            return 0
        s=self.dfs(node.left)
        self.dfs(node.right)
        self.sumi+=s
        if node.left is None and node.right is None:
            return node.val
        return 0
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        self.sumi=0
        self.dfs(root)
        return self.sumi