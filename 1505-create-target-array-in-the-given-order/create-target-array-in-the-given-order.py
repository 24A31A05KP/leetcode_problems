class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=[0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)-1,index[i],-1):
                target[j]=target[j-1]
            target[index[i]]=nums[i]
        return target