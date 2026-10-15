class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        count0=count1=max0=max1=0
        for i in s:
            if i=='0':
                count0+=1
                count1=0
            else:
                count1+=1
                count0=0
            max0=max(max0,count0)
            max1=max(max1,count1)
        return max1>max0