class Solution:
    def transpose(self, mat):
        leng=len(mat)
        for i in range(leng):
            for j in range(i+1, leng):
                mat[i][j], mat[j][i]=mat[j][i], mat[i][j]
        
        return mat