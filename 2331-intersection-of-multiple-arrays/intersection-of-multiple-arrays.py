class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        result=[]
        freq=[0]*1001
        for i in nums:
            for j in i:
                freq[j]+=1
        for idx,val in enumerate(freq):
            if val==n:
                result.append(idx)
        return result