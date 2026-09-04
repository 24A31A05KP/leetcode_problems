class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxi=-1
        for i in range(len(nums)):
            mini=float('inf')
            maxi=max(maxi,nums[i])
            for j in range(i,len(nums)):
                mini=min(mini,nums[j])
            if maxi-mini<=k:
                return i
        return -1