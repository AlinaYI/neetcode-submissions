class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i,j):
            seen.add((i,j))
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<row and 0<=nj<col and (ni,nj) not in seen and grid[ni][nj] == "1":
                    dfs(ni,nj)
            
            
        seen = set()
        row, col = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in seen:
                    dfs(i,j)
                    res += 1
        return res