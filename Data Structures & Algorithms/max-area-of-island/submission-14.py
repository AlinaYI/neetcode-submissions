class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        def bfs(i,j):
            q = deque([(i,j)])
            seen.add((i,j))
            res = 1
            while q:
                i, j = q.popleft()
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if 0<=ni<row and 0<=nj<col and(ni,nj) not in seen and grid[ni][nj] == 1:
                        seen.add((ni,nj))
                        q.append((ni,nj))
                        res += 1
            return res
        
        res = 0
        seen = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(row):
            for j in range(col):
                if (i,j) not in seen and grid[i][j] == 1:
                    area = bfs(i,j)
                    res = max(area, res)
        return res
        