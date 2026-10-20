class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        directions={
            "R":(0,1),"D":(1,0),
            "L":(0,-1),"U":(-1,0)
            }
        seen=set()
        seen.add((0,0))
        i=j=0
        while True:
            a,b=directions[grid[i][j]]
            ni,nj=i+a,j+b

            if not(0<=ni<len(grid) and 0<=nj<len(grid[0])) or (ni,nj) in seen:
                break
            seen.add((ni,nj))
            i,j=ni,nj
        return [i,j]
        # seen=set()
        # i=0
        # j=0
        
        # while 0<=i<len(grid) and 0<=j<len(grid[0]):
        #     if (i,j) in seen:
        #         return [i,j]
        #     seen.add((i,j))
        #     a,b=directions[grid[i][j]]
        #     last_visit=[i,j]
        #     i+=a
        #     j+=b

        # return last_visit
