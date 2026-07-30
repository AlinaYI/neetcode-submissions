class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i,j) not in seen and grid[i][j] == 1:
                
                seen.add((i,j))
                temp = 1
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    temp += dfs(ni,nj)
                return temp
            else:
                return 0
        
        seen = set()
        res = 0
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in seen:
                    area = dfs(i,j)
                    res = max(res, area)
        return res