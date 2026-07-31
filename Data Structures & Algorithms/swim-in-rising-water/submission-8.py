class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # heigh, i, j
        minHeap = [(grid[0][0], 0, 0)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        row, col = len(grid), len(grid[0])
        seen = set()
        while minHeap:
            height, i, j = heapq.heappop(minHeap)
            
            if i == row-1 and j == col-1:
                return height
            
            if (i,j) in seen:
                continue

            seen.add((i,j))
            for di,dj in directions:
                ni,nj=i+di, j+dj
                if (ni,nj) not in seen and 0<=ni<row and 0<=nj<col:
                    newHeight = max(height, grid[ni][nj])
                    heapq.heappush(minHeap, (newHeight, ni, nj))
