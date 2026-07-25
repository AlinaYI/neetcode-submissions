class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        bfs - traverse grid
        要选最小的，每一条路都会有weighted，所以用dijaski
        '''

        # time, i, j
        min_heap = [(grid[0][0], 0, 0)]
        seen = set() # 就是所有的防止loop
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while min_heap:
            curr_time, i, j = heapq.heappop(min_heap)

            if (i,j) in seen:
                continue
            
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return curr_time

            seen.add((i, j))
            for di, dj in directions:
                ni, nj  = i + di, j + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in seen:
                    new_time = max(curr_time, grid[ni][nj])
                    heapq.heappush(min_heap, (new_time, ni, nj))
