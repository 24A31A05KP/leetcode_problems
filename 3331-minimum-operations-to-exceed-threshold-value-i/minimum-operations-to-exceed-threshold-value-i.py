class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operations=0
        for i in nums:
            if i<k:
                operations+=1
        return operations