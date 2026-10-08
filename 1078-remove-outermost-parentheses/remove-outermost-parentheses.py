class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth=0
        answer=[]
        for i in s:
            if i == '(':
                if depth !=0:
                    answer.append(i)
                depth+=1
            else:
                depth-=1
                if depth !=0:
                    answer.append(i)
        return "".join(answer)