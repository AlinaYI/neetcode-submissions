class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dijkstra
        minHeap = [ (grid[0][0], 0, 0) ]
        res = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        row, col = len(grid), len(grid[0])
        seen = set()
        while minHeap:
            heigh, i, j = heapq.heappop(minHeap)
            
            if i == row-1 and j == col-1:
                res = heigh
            
            if (i,j) in seen:
                continue
                
            seen.add((i,j))
            for di,dj in directions:
                ni,nj=i+di,j+dj
                if 0<=ni<row and 0<=nj<col and (ni,nj) not in seen:
                    newHeigh = max(grid[ni][nj], heigh)
                    heapq.heappush(minHeap, (newHeigh, ni, nj))
        return res