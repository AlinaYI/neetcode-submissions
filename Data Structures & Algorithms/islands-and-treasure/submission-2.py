class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # dfs要多一个对比grid[i][j]大小，因为是depth first，所以当前的step不一定是最小的
        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        # 所有的start都在q里面
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        EMPTY = 2147483647
        while q:
            i, j = q.popleft()
            for di, dj in directions:
                ni, nj = di + i, dj + j
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == EMPTY:
                    grid[ni][nj] = grid[i][j] + 1
                    q.append((ni, nj))
        