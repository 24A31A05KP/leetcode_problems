# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result=[]
        stack=[(root,'')]
        while stack:
            node,path=stack.pop()
            path+=str(node.val)+'->'
            if node.left is None and node.right is None:
                result.append(path[:len(path)-2])
            if node.right:
                stack.append((node.right,path))
            if node.left:
                stack.append((node.left,path))
        return result
