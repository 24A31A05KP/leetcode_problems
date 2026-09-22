class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        zeros=0
        max_l=0
        for right in range(len(nums)):
            if nums[right]==0:
                zeros+=1
            while zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            max_l=max(max_l,right-left+1)
        return max_l