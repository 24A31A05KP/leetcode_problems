class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ps=0
        boundary=0
        for i in nums:
            ps+=i
            if ps==0:
                boundary+=1
        return boundary