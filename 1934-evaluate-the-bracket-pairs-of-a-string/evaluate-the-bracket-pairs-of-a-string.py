class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d={}
        for key,val in knowledge:
            d[key]=val
        key=""
        ans=""
        incheck=False
        for ch in s:
            if ch=='(':
                incheck=True
                key=""
            elif ch==')':
                incheck=False
                ans+=d.get(key,'?')
            elif incheck:
                key+=ch
            else:
                ans+=ch
        return ans