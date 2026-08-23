class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        dsu
        把所有的cell变成一个node，然后排序
        一个node，一个node 连接
        如果当前的node是右下角的， 就return 当前的hight, 就直接return
        tc: O(mnlogmn) sc: Omn

        binary search 
        因为这里的答案是单调的，每次path都要取最大的，所以这里可以用binary search
        range 就是grid[0][0] -- len(grid)*len(grid)
        如果当前的mid， 带入能从左上跑到右下，那就是valid， 然后再看有没有比这个更小的值
        tc: (binary search 次数)log(mn) * mn (每次dfs的tc)
        sc: O(mn) --> seen

        dijkstra
        就是把这个当成weighted map看，加入minHeap，每次选尽量小的值
        直到到右下
        不用建graph，直接用grid来search 四个方向
        tc: Omn * logmn --> heap logmn
        sc: Omn
        '''

        def valid(height):
            seen = {(0,0)}
            q = deque([(0,0)])
            
            while q:
                i, j = q.popleft()

                if i == row-1 and j == col-1:
                    return True
                
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if 0<=ni<row and 0<=nj<col and (ni,nj) not in seen and grid[ni][nj] <= height:
                        seen.add((ni,nj))
                        q.append((ni,nj))
            return False

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        row, col = len(grid), len(grid[0])
        left, right = max(grid[0][0], grid[row-1][col-1]), len(grid)*len(grid)
        while left <= right:
            mid = left + (right-left)//2

            if valid(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

