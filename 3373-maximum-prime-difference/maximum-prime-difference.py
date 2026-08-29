class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        mini_idx=-1
        maxi_idx=-1
        for i in range(len(nums)):
            j=2
            trigger=0
            if nums[i]<2:
                continue
            while j*j<=nums[i]:
                if nums[i]%j==0:
                    break
                j+=1
            else:
                mini_idx=i
                break
        for i in range(len(nums)-1,-1,-1):
            j=2
            trigger=0
            if nums[i]<2:
                continue
            while j*j<=nums[i]:
                if nums[i]%j==0:
                    break
                j+=1
            else:
                maxi_idx=i
                break
        return maxi_idx-mini_idx            