class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # pacific_set
        # atlantic_set
        # in both set

        def dfs(i,j, seen_set):
            
            if 0 <= i < len(heights) and 0 <= j < len(heights[0]) and (i,j) not in seen_set:
                seen_set.add((i,j))

                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    # ni, nj > i, j
                    if 0 <= ni < len(heights) and 0 <= nj < len(heights[0]) and (ni,nj) not in seen_set and heights[ni][nj] >= heights[i][j]:
                        dfs(ni, nj, seen_set)
            else:
                return
        
        res = []
        pacific_set = set()
        atlantic_set = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        for i in range(len(heights)):
            dfs(i, 0, pacific_set) # first col
            dfs(i, len(heights[0])-1, atlantic_set)

        for j in range(len(heights[0])):
            dfs(0, j ,pacific_set) # first row
            dfs(len(heights)-1, j, atlantic_set)
        
        for cell in pacific_set:
            if cell in atlantic_set:
                res.append([cell[0], cell[1]])
        return res

       
