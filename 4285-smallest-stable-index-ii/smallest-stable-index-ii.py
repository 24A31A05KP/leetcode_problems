class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mini_arr=[0]*len(nums)
        mini=nums[-1]
        maxi=nums[0]
        for i in range(len(nums)-1,-1,-1):
            mini=min(mini,nums[i])
            mini_arr[i]=mini
        for i in range(len(nums)):
            maxi=max(maxi,nums[i])
            if maxi-mini_arr[i]<=k:
                return i
        return -1