class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        s=set()
        n=len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if digits[i]!=0 and i!=j and j!=k and k!=i:
                        d=100*digits[i]+10*digits[j]+digits[k]
                        if d%2==0:
                            s.add(d)
        return len(s)