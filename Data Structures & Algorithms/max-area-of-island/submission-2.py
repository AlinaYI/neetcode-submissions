class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i,j) in seen or grid[i][j] == 0:
                return 0
            
            seen.add((i,j))
            area = 1
            for di, dj in direction:
                ni, nj = i + di, j + dj
                area += dfs(ni, nj)
            return area

        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        seen = set()
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in seen:
                    res = max(res, dfs(i,j))
        return res