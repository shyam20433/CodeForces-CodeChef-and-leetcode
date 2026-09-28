class Solution:
    def celebrity(self, mat):
        # code here
        i=0
        j=len(mat)-1
        while i<j:
            
            if mat[j][i]==1:
                j-=1
            else:
                i+=1
        candidate=i
        for i in range(len(mat)):
            if i==candidate:
                continue
            if  mat[candidate][i] or not mat[i][candidate]:
                return -1
        return candidate