class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        maxi=float('-inf')
        for i in strs:
            if i.isdigit():
                maxi=max(maxi,int(i))
            else:
                maxi=max(maxi,len(i))
        return maxi