class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        union find -- dsu
        dijkstra
        binary search
        '''

        row = len(grid)
        col = len(grid[0])
        # height, row, col
        min_heap = [(grid[0][0], 0, 0)]
        seen = set()
        directions = [(0,1), (0,-1),(1,0),(-1,0)]
    
        while min_heap:
            height, i, j = heapq.heappop(min_heap)

            if i == row-1 and j == col-1:
                return height
            
            if (i,j) in seen:
                continue
            
            seen.add((i,j))
            for di, dj in directions:
                ni, nj = di+i, dj+j
                if 0<=ni<row and 0<=nj<col and (ni, nj) not in seen:
                    new_height = max(height, grid[ni][nj])
                    heapq.heappush(min_heap, (new_height, ni, nj))
        