class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%len(nums)]:
                count+=1
                pos=i
        if count>1:
            return -1
        if count==0:
            return 0
        return len(nums)-pos-1