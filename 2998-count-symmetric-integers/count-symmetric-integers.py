class Solution:
    def symmetric(self,x):
        x1=str(x)
        if len(x1)%2!=0:
            return False
        j=len(x1)-1
        sum1=sum2=0
        for i in range(len(x1)//2):
            sum1+=int(x1[i])
            sum2+=int(x1[j])
            j-=1
        return sum1==sum2

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        if high<=10:
            return 0
        count=0
        for i in range(low,high+1):
            if self.symmetric(i):
                count+=1
        return count