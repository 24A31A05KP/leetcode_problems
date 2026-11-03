class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        ans=[0]*len(code)
        if k==0:
            return ans
        for i in range(len(code)):
            if k>0:
                for j in range(1,k+1):
                    ans[i]+=code[(i+j)%len(code)]
            else:
                for j in range(abs(k),0,-1):
                    ans[i]+=code[(i-j)%len(code)]
        return ans