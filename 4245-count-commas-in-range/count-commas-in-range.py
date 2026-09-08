class Solution:
    def countCommas(self, n: int) -> int:
        l=len(str(n))
        if l<4:
            return 0
        count_comma=0
        for i in range(1000,n+1):
            l1=len(str(i))
            while l1>=4:
                count_comma+=1
                l1-=3
        return count_comma