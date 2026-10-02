class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        s1=""
        for i in s:
            freq[i]=freq.get(i,0)+1
        result=dict(sorted(freq.items(),key=lambda x:x[1],reverse=True))
        for i in result:
            s1+=i*result[i]
        return s1