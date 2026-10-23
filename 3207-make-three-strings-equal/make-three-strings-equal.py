class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if s1[0]!=s2[0] or s2[0]!=s3[0]:
                return -1
        l=min(len(s1),len(s2),len(s3))
        i=0
        while i<l:
            if s1[i]!=s2[i] or s2[i]!=s3[i]:
                break
            i+=1
        print(i)
        return len(s1)+len(s2)+len(s3)-(3*i)