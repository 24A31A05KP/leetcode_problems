class Solution:
    def canAliceWin(self, n: int) -> bool:
        x=10
        ans=False
        while n>=x:
            n-=x
            x-=1
            ans=not ans
        return ans