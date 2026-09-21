class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n=len(cardPoints)
        if k==0:
            return 0
        if k<0 or k>n:
            return -1
        if k==n:
            return sum(cardPoints)
        sumi=0
        for i in range(k):
            sumi+=cardPoints[i]
        maxi=sumi
        i=k-1
        j=n-1
        while i!=-1:
            sumi+=cardPoints[j]-cardPoints[i]
            maxi=max(maxi,sumi)
            i-=1
            j-=1
        return maxi