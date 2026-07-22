class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i,j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i,j) not in seen and grid[i][j] == "1":
                seen.add((i,j))
                dfs(i + 1 ,j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
            
            return

        res = 0
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in seen:
                    dfs(i, j)
                    res += 1
        return res
