# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        result=[]
        ans=[]
        stack=[(root,targetSum,[])]
        while stack:
            node,remaining,ans=stack.pop()
            ans=ans+[node.val]
            remaining-=node.val
            if node.left is None and node.right is None:
                if remaining==0:
                    result.append(ans)
            if node.right:
                stack.append((node.right,remaining,ans))
            if node.left:
                stack.append((node.left,remaining,ans))
        return result