class Solution:
    def rob(self, nums: list[int]) -> int:
        max1=max2=0
        for i in range(len(nums)):
            t=max(max1,max2+nums[i])
            max2=max1
            max1=t
        return max1