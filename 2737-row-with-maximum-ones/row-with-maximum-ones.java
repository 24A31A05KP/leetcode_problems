class Solution {
    public int[] rowAndMaximumOnes(int[][] mat) {
        int ind=0,mc=0;
       for(int i=0;i<mat.length;i++){
        int c=0;
        for(int j=0;j<mat[0].length;j++){
            if(mat[i][j]==1) c++;
        }
        if(mc<c){
            mc=c;
            ind=i;
        }
        
       } 
       return new int[]{ind,mc};
    }
}