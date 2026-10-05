class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=0
        depth=0
        stack=[]
        for i,val in enumerate(s):
            if val=='(':
                depth+=1
            else:
                depth-=1
                if s[i-1]=='(':
                    score+=2**depth
        return score