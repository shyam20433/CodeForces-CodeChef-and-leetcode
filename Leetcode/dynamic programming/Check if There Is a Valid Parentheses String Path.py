class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        if grid[0][0]==")":
            return False
        seen=set()
        
        def backtrack(balance,i,j):
            if i>=len(grid) or j>=len(grid[0]):
                return False
            if i>len(grid) or j>len(grid[0]):
                return False
            if grid[i][j]=="(":
                balance+=1
            if grid[i][j]==")":
                balance-=1
            if balance<0:
                return False
            if  i==len(grid)-1 and j ==len(grid[0])-1:
                return balance==0
            check=(balance,i,j)
            if check in seen:
                return False
            seen.add(check)
            return backtrack(balance,i+1,j) or backtrack(balance,i,j+1)
                
        return backtrack(0,0,0)

        