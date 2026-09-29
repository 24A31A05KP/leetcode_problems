class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sumi=0
        for i in range(len(nums)):
            if bin(i).count('1')==k:
                sumi+=nums[i]
        return sumi