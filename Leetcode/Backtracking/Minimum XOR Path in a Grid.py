class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        #  Wont work beacause ^ is not monotonic so next value wont decide the minimum value so greedy dp wont work
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if i==0 and j==0:
        #             continue
        #         if i>0 and j>0:
        #             grid[i][j]=min(grid[i][j]^grid[i-1][j],grid[i][j]^grid[i][j-1])
        #         elif i>0:
        #             grid[i][j]^=grid[i-1][j]
        #         elif j>0:
        #             grid[i][j]^=grid[i][j-1]
        # print(grid)
        # return grid[-1][-1]
                
        #approach two 
        n=len(grid)
        m=len(grid[0])
        dp=[[[-1]*1024 for i in range(m)]for j in range(n)]

        def backtrack(i,j,temp):
            if i>=n or j>=m:
                return float('inf')
            
            temp^=grid[i][j]
            if i==n-1 and j==m-1:
                return temp
            
            if dp[i][j][temp]!=-1:
                return dp[i][j][temp]
            
            right=backtrack(i,j+1,temp)
            down=backtrack(i+1,j,temp)
            dp[i][j][temp]=min(right,down)
            return dp[i][j][temp]
            
        return backtrack(0,0,0)

            
