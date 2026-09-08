class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        count_comma=0
        for i in range(1000,n+1):
            count_comma+=1
        return count_comma