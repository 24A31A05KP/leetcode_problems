class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr)<3:
            return False
        inc=False
        dec=False
        for i in range(1,len(arr)):
            if arr[i-1]==arr[i]:
                return False
            elif arr[i-1]<arr[i]:
                if dec:
                    return False
                inc=True
            elif arr[i-1]>arr[i]:
                if not inc:
                    return False
                dec=True
        return inc and dec