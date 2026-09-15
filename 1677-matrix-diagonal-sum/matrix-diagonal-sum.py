class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result=0
        n=len(mat)
        for i in range(n):
            result+=mat[i][i]+mat[i][n-i-1]
        return result if n%2==0 else result-mat[n//2][n//2]