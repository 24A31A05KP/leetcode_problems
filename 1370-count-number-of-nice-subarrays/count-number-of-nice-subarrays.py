class Solution:
    def atmost(self,nums,k):
        if k<0:
            return 0
        count=0
        left=0
        odd=0
        for right in range(len(nums)):
            odd+=nums[right]%2
            print(odd)
            while odd>k:
                odd-=nums[left]%2
                left+=1
            count+=right-left+1
        return count
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
       return self.atmost(nums,k)-self.atmost(nums,k-1)