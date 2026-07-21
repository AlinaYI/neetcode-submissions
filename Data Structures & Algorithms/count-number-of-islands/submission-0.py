class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i,j) in seen or grid[i][j] == "0":
                return

            seen.add((i,j))
            for di, dj in directions:
                ni, nj = di + i, dj + j
                dfs(ni, nj)
            
        res = 0
        seen = set()
        directions = [(0,1), (0,-1),(1,0),(-1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    dfs(i,j)
                    res += 1
        return res