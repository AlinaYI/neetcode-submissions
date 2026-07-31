class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i,j,seen):
            
            seen.add((i,j))
            for di,dj in directions:
                ni,nj = i+di, j+dj
                if 0<=ni<row and 0<=nj<col and (ni,nj) not in seen and heights[ni][nj] >= heights[i][j]:
                    dfs(ni,nj,seen)
        
        
        atlanticSet = set()
        pacificSet = set()
        for i in range(row):
            dfs(i,0,pacificSet)
            dfs(i,col-1, atlanticSet)
        
        for j in range(col):
            dfs(0, j, pacificSet)
            dfs(row-1, j, atlanticSet)
        
        res = []
        for i,j in pacificSet:
            if (i,j) in atlanticSet:
                res.append([i,j])
        return res