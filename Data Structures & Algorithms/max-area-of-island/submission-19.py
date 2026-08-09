class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j):
            area = 1
            seen.add((i,j))
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<row and 0<=nj<col and (ni,nj) not in seen and grid[ni][nj] == 1:
                    area += dfs(ni, nj)
            return area

        row, col = len(grid), len(grid[0])
        seen = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in seen:
                    area = dfs(i,j)
                    res = max(area, res)
        return res