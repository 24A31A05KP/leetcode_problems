# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue=deque([root])
        result=[]
        while queue:
            lvl_size=len(queue)
            lvl=[]
            for i in range(lvl_size):
                node=queue.popleft()
                lvl.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(lvl[-1])
        return result