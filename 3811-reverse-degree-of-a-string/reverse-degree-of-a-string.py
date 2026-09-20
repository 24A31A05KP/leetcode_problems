class Solution:
    def reverseDegree(self, s: str) -> int:
        sumi=0
        for i in range(len(s)):
            sumi+=(26-(ord(s[i])-97))*(i+1)
        return sumi