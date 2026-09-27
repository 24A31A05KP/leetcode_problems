# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self,node,target,temp):
        if node is None:
            return
        temp.append(node)
        if node==target:
            return True
        if self.dfs(node.left,target,temp):
            return True
        if self.dfs(node.right,target,temp):
            return True
        temp.pop()
        return False
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        arr1=[]
        arr2=[]
        self.dfs(root,p,arr1)
        self.dfs(root,q,arr2)
        m=None
        for i in range(min(len(arr1),len(arr2))):
            if arr1[i]==arr2[i]:
                m=arr1[i]
            else:
                break
        return m