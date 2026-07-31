class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        def dfs(i,j):
            area = 0
            if 0<=i<row and 0<=j<col and (i,j) not in seen and grid[i][j] == 1:
                seen.add((i,j))
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    area += dfs(ni, nj)
            else: 
                return 0
            return 1 + area
            
        
        res = 0
        seen = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(row):
            for j in range(col):
                if (i,j) not in seen and grid[i][j] == 1:
                    area = dfs(i,j)
                    res = max(area, res)
        return res
        