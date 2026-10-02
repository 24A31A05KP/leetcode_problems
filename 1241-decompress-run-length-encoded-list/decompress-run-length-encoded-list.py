class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        ans=[]
        for i in range(len(nums)):
            if 2*i+1<len(nums):
                ans.extend([nums[2*i+1]]*nums[2*i])
        return ans