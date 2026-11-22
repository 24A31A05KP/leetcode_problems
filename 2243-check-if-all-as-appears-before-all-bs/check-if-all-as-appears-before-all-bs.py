class Solution:
    def checkString(self, s: str) -> bool:
        outlier=False
        for i in range(len(s)):
            if s[i]=='b':
                outlier=True
            if outlier and s[i]=='a':
                return False
        return True