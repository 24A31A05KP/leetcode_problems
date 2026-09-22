class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        idx=-1
        maxi=float('-inf')
        for i in range(len(nums)):
            if maxi<nums[i]:
                maxi=nums[i]
                idx=i
        if maxi>(2**31)-1 or maxi<-(2**31):
            return 0
        return idx