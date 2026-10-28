class Solution:
    def isPalindromic(self, s: str) -> bool:
        bin_str=""
        for i in s:
            bin_str+=bin(ord(i))[2:].zfill(8)
        return bin_str==bin_str[::-1]