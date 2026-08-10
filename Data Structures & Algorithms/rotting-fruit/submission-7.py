class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        row, col = len(grid), len(grid[0])
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        fresh = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        res = 0
        while q and fresh > 0:
            qLen = len(q)
            for _ in range(qLen):
                i, j = q.popleft()

                for di,dj in direction:
                    ni, nj = i+di, j+dj
                    if 0<=ni<row and 0<=nj<col and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        q.append((ni,nj))
                        fresh -= 1
            res += 1
        return res if fresh == 0 else -1
