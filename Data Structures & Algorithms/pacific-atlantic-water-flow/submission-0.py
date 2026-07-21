class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()

        directions = [(0,1), (0,-1),(1,0),(-1,0)]
        
        def dfs(i, j, seen):
            if i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0]) or (i,j) in seen:
                return 

            seen.add((i,j))

            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 <= ni < len(heights) and 0<=nj<len(heights[0]) and (ni,nj) not in seen and heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, seen)
        
        for j in range(len(heights[0])):
            dfs(0, j, pacific)
        for i in range(len(heights)):
            dfs(i, 0, pacific)

        for j in range(len(heights[0])):
            dfs(len(heights)-1, j, atlantic)
        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1, atlantic)
        
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        return res
