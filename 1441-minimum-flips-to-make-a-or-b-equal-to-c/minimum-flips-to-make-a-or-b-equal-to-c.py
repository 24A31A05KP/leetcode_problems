class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count=0
        while a or b or c:
            rem1=a%2
            rem2=b%2
            rem3=c%2
            if rem3==0:
                if rem1==1:
                    count+=1
                if rem2==1:
                    count+=1
            else:
                if rem1==0 and rem2==0:
                    count+=1
            a//=2
            b//=2
            c//=2
        return count