class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:

        def island(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]!=0:
                curr=grid[i][j]
                grid[i][j]=0
                return curr+island(i+1,j) + island(i-1,j) + island(i,j+1) + island(i,j-1)
            return 0
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    total=island(i,j)
                    if total!=0 and total%k==0:
                        count+=1
        return count