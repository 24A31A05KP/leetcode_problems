class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        s=set()
        nums.sort()
        j=len(nums)-1
        for i in range(len(nums)//2):
            s.add((nums[i]+nums[j])/2)
            j-=1
        return len(s)