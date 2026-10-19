class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less=equal=0
        for i in nums:
            if i<target:
                less+=1
            elif i==target:
                equal+=1
        return list(range(less,less+equal))