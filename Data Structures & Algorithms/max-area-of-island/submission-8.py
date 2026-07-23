class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j):

            grid[i][j] = 0
            area = 1
            for di, dj in directions:
                ni, nj = di + i, dj +j
                if 0 <= ni < len(grid) and 0 <= nj <len(grid[0]) and grid[ni][nj] == 1:
                    area += dfs(ni, nj) 
            return area

        res = 0
        directions = [(0,1), (0,-1),(1,0), (-1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    res = max(res, area)
        return res