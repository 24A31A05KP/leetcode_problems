class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v=c=0
        for i in s:
            if i in {'a','e','i','o','u'}:
                v+=1
            elif i.isalpha():
                c+=1
        if c>0:
            return v//c
        return 0