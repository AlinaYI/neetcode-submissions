class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j):
            area = 0
            if 0 <= i <len(grid) and 0<=j<len(grid[0]) and (i,j) not in seen and grid[i][j] == 1:
                seen.add((i,j))
                for di,dj in directions:
                    ni, nj = i+di, j+dj
                    area += dfs(ni, nj)
                return area + 1
            else:
                return  0
            return area + 1
        
        res = 0
        seen = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in seen:
                    area = dfs(i,j)
                    res = max(area,res)
        return res