class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        EMPTY = 2147483647
        def dfs(i,j, step):

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            
            if grid[i][j] >= step or grid[i][j] == EMPTY:
                grid[i][j] = step
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    dfs(ni, nj, step + 1)

        directions = [(0,1), (0,-1), (1,0),(-1,0)]
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    dfs(i, j, 0)
