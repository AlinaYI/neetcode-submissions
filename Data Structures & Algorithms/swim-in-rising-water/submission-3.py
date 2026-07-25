class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        bfs - traverse grid
        要选最小的，每一条路都会有weighted，所以用dijaski
        '''
        def bfs(val):
            seen = set()
            q = deque([(0,0)])
            directions = [(0,1), (1, 0), (-1,0), (0,-1)]
            seen.add((0,0))
            while q:
                i, j = q.popleft()

                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    return True
                
                for di, dj in directions:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in seen and grid[ni][nj] <= val:
                        seen.add((ni,nj))
                        q.append((ni,nj))
            return False


        left = max(grid[0][0], grid[len(grid)-1][len(grid[0])-1])
        right = len(grid)*len(grid)

        while left < right:
            mid = left + (right-left)//2

            if bfs(mid):
                right = mid
            else:
                left = mid +1
        return left
