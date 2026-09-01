class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sub=0
        for i in range(len(arr)):
            sub_sum=0
            for j in range(i,len(arr)):
                sub_sum+=arr[j]
                if (j-i+1)%2!=0:
                    total_sub+=sub_sum
        return total_sub