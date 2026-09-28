class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l_s=0
        freq={}
        max_freq=0
        i=0
        for j in range(len(s)):
            freq[s[j]]=freq.get(s[j],0)+1
            max_freq=max(max_freq,freq[s[j]])
            sub=j-i+1
            if sub-max_freq>k:
                freq[s[i]]-=1
                i+=1
            l_s=max(l_s,j-i+1)
        return l_s