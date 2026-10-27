class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        freq={}
        ans=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        while freq:
            freq1=sorted(freq.keys())
            for i in freq1:
                ans.append(i)
                freq[i]-=1
                if freq[i]==0:
                    del freq[i]
        return ans