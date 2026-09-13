class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n=len(words)
        d=set()
        result=[]
        for i in words:
            for j in i:
                d.add(j)
        for i in d:
            d1=float('inf')
            for word in words:
                d1=min(d1,word.count(i))
            while d1>0:
                result.append(i)
                d1-=1
        return result