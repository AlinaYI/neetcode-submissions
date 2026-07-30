class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i,j,seen_set):
            seen_set.add((i,j))
            for di, dj in directions:
                ni, nj = di+i, dj+j
                if 0<=ni<len(heights) and 0<=nj<len(heights[0]) and (ni,nj) not in seen_set and heights[ni][nj] >= heights[i][j]:
                    dfs(ni,nj,seen_set)
        
        pacific_set = set()
        atlantic_set = set()
        for i in range(len(heights)):
            dfs(i, 0, pacific_set)
            dfs(i, len(heights[0])-1, atlantic_set)
        
        for i in range(len(heights[0])):
            dfs(0, i, pacific_set)
            dfs(len(heights)-1, i, atlantic_set)
        
        res = []
        for i, j in atlantic_set:
            if (i,j) in pacific_set:
                res.append([i,j])
        return res