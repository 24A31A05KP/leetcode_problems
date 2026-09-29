class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        freq={}
        count=0
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]]=[i]
            else:
                freq[nums[i]].append(i)
        for i in freq:
            if len(freq[i])==3:
                if freq[i][1]-freq[i][0]==freq[i][2]-freq[i][1]:
                    count+=1
        return count