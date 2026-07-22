class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque([])
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        res = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
               
                for di,dj in directions:
                    ni, nj = i + di, j + dj
                    if 0<= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        q.append((ni,nj))
            res += 1

        return res if fresh == 0 else -1