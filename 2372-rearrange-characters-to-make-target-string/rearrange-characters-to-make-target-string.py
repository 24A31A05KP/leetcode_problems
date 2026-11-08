class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        t={}
        s1={}
        for i in target:
            t[i]=t.get(i,0)+1
        for i in s:
            if i in t:
                s1[i]=s1.get(i,0)+1
        if len(t)!=len(s1):
            return 0
        return min(s1[i]//t[i] for i in t)