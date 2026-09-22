class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq={}
        for idx,val in enumerate(nums):
            if val in freq:
                if idx-freq[val]<=k:
                    return True
                else:
                    freq[val]=idx
            else:
                freq[val]=idx
        return False