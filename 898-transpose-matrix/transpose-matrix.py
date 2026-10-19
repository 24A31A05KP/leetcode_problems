class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        row,col=len(matrix),len(matrix[0])
        trans=[[0 for _ in range(row)] for _ in range(col)]
        for i in range(row):
            for j in range(col):
                trans[j][i]=matrix[i][j]
        return trans