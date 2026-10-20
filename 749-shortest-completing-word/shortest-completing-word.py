class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        lic_map={}
        result=""
        for i in licensePlate:
            if i.isalpha():
                lic_map[i.lower()]=lic_map.get(i.lower(),0)+1
        for word in words:
            freq=lic_map.copy()
            for j in word:
                if j in freq:
                    freq[j]-=1
                    if freq[j]==0:
                        del freq[j]
            if not freq:
                if len(result)>len(word) or result=='':
                    result=word
        return result