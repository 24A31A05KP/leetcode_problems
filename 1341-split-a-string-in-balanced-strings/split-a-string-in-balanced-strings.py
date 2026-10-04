class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans=0
        bal=0
        for i in s:
            if i=='L':
                bal+=1
            elif i=='R':
                bal-=1
            if bal==0:
                ans+=1
        return ans