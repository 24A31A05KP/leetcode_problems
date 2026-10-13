class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        arr=sorted([i*i for i in nums])
        sum=0
        j=n-1
        for i in range(n//2):
            sum+=arr[j]-arr[i]
            j-=1
        if n%2!=0:
            sum+=arr[n//2]
        return sum