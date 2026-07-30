class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # bfs
        q = deque([])
        EMPTY = 2147483647
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        while q:
            i, j = q.popleft()
            
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<len(grid) and 0 <=nj<len(grid[0])and grid[ni][nj] == EMPTY:
                    grid[ni][nj] = grid[i][j] + 1
                    q.append((ni,nj))