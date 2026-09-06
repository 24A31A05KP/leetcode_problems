# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False
        stack1=[root.left]
        stack2=[root.right]
        while stack1 and stack2:
            node1=stack1.pop()
            node2=stack2.pop()
            if node1.val!=node2.val:
                return False
            if node1.left and node2.right:
                stack1.append(node1.left)
                stack2.append(node2.right)
            elif node1.left or node2.right:
                return False
            if node1.right and node2.left:
                stack1.append(node1.right)
                stack2.append(node2.left)
            elif node1.right or node2.left:
                return False
        return True