class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque([])
        row, col = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        EMPTY = 2147483647
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append( (i,j) )
        
        while q:
            i, j = q.popleft()

            for di, dj in directions:
                ni,nj = i+di, j+dj
                if 0<=ni<row and 0<=nj<col and grid[ni][nj] == EMPTY:
                    grid[ni][nj] = grid[i][j] + 1
                    q.append((ni,nj))
        return
            