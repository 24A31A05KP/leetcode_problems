class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sum=0
        for ch in columnTitle:
            sum=sum*26+ord(ch)-ord('A')+1
        return sum