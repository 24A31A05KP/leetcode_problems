class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        max_depth=0
        for i in s:
            if i=='(':
                depth+=1
            elif i==')':
                depth-=1
            max_depth=max(max_depth,depth)
        return max_depth