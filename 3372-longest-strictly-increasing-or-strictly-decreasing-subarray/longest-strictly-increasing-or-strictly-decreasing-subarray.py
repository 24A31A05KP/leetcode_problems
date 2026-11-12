class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc=[]
        dec=[]
        for i in range(len(nums)):
            inc1=[]
            dec1=[]
            for j in range(i,len(nums)):
                if (len(inc1)==0 or inc1[-1]<nums[j]):
                    inc1.append(nums[j])
                else:break
            for j in range(i,len(nums)):
                if (len(dec1)==0 or dec1[-1]>nums[j]):
                    dec1.append(nums[j])
                else:break
            if len(inc1)>len(inc):
                inc=inc1
            if len(dec1)>len(dec):
                dec=dec1
        return max(len(inc),len(dec))