class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # binary search
        # dsu
        # dijkstra

        minHeap = [ (grid[0][0], 0, 0) ]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        seen = set()
        while minHeap:

            currH, i, j = heapq.heappop(minHeap)

            if i == len(grid)-1 and j == len(grid[0])-1:
                return currH
            
            if (i,j) in seen:
                continue
            
            seen.add((i,j))
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and (ni, nj) not in seen:
                    maxH = max(currH, grid[ni][nj])
                    heapq.heappush(minHeap, (maxH, ni, nj))
        return 0
            