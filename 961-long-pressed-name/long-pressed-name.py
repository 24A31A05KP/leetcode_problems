class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i=j=0
        while j<len(typed):
            if i<len(name) and name[i]==typed[j]:
                i+=1
            elif j==0 or typed[j-1]!=typed[j]:
                return False
            j+=1
        return i==len(name)