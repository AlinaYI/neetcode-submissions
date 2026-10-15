class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(i, j, seen):

            seen.add( (i,j) )
            for di,dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<len(heights) and 0<=nj<len(heights[0]) and heights[i][j] <= heights[ni][nj] and (ni,nj) not in seen:
                    dfs(ni, nj, seen)

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        pacificSet = set()
        atlanticSet = set()

        for i in range(len(heights)):
            dfs(i, 0, pacificSet)
            dfs(i, len(heights[0])-1, atlanticSet)
        
        for j in range(len(heights[0])):
            dfs(0, j, pacificSet)
            dfs(len(heights)-1, j, atlanticSet)

        res = []
        for position in pacificSet:
            if position in atlanticSet:
                res.append(position)
        return res