class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        EMPTY = 2147483647
        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            i,j = q.popleft()
            
            for di,dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj] == EMPTY:
                    grid[ni][nj] = 1 + grid[i][j]
                    q.append((ni,nj))

