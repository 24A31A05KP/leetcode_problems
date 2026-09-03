class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxi_c=-1
        idx=float('inf')
        for i in range(len(mat)):
            count=0
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    count+=1
            if count>maxi_c:
                maxi_c=count
                idx=i
        return [idx,maxi_c]