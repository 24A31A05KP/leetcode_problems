class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        freq={}
        for i in words:
            for j in i:
                freq[j]=freq.get(j,0)+1
        for i in freq:
            if freq[i]%len(words)!=0:
                return False
        return True