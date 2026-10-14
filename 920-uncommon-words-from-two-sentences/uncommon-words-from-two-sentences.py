class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        freq={}
        result=[]
        s1=s1.split()
        s2=s2.split()
        for i in s1:
            freq[i]=freq.get(i,0)+1
        for i in s2:
            freq[i]=freq.get(i,0)+1
        for i in freq:
            if freq[i]==1:
                result.append(i)
        return result