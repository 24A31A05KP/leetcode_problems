class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        addition=0
        depth=0
        for ch in s:
            if ch=='(':
                depth+=1
            else:
                if depth>0:
                    depth-=1
                else:
                    addition+=1
        return depth+addition