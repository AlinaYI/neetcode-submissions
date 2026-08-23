class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(i,j,seen):
            seen.add((i,j))
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<row and 0<=nj<col and heights[ni][nj] >= heights[i][j] and (ni, nj) not in seen:
                    dfs(ni, nj, seen)

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        row, col = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        for i in range(row):
            dfs(i, 0, pacific)
            dfs(i, col-1, atlantic)
        
        for j in range(col):
            dfs(0, j, pacific)
            dfs(row-1, j, atlantic)
        
        res = []
        for i,j in pacific:
            if (i,j) in atlantic:
                res.append([i,j])
        return res
        

                