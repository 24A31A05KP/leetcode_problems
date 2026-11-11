class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq={}
        result=[]
        for i in nums1:
            freq[i]=freq.get(i,0)+1
        for i in nums2:
            if i in freq:
                result.append(i)
                freq[i]-=1
                if freq[i]==0:
                    del freq[i]
        return result