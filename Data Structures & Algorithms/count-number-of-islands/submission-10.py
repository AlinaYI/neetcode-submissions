class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i, j):
            seen.add((i,j))
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<len(grid) and 0<= nj<len(grid[0]) and (ni,nj) not in seen and grid[ni][nj] == '1':
                    dfs(ni, nj)
            

        res = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in seen:
                    dfs(i,j)
                    res += 1
        return res