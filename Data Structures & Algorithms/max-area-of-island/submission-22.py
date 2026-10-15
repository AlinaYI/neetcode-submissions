class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            area = 1
            seen.add((i,j))

            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and (ni,nj) not in seen and grid[ni][nj] == 1:
                    area += dfs(ni, nj)
            return area
        
        area = 0
        seen = set()
        directions = [(0,1), (0,-1),(-1,0),(1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in seen:
                    area = max(area, dfs(i,j))
        return area