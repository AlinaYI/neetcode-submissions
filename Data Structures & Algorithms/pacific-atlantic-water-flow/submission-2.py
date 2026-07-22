class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # 得看是不是都能到pacific/atlantic
        # 要是一个个去dfs/bfs，那就是会有很多重复计算
        # 所以可以从pacific的边 -> atlantic边， atlantic边 -> pacific的边
        # 然后在两个set里面，那就是连通的

        pacific = set()
        atlantic = set()
        directions = [(0,1), (0,-1),(1,0),(-1,0)]
        # 因为是反过来的，所以这里要找比grid[i][j]大的cell
        def dfs(i, j, seen):
            seen.add((i,j))
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(heights) and 0 <= nj < len(heights[0]) and (ni,nj) not in seen and heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, seen)
        
        for i in range(len(heights)):
            dfs(i, 0, pacific)
            dfs(i, len(heights[0])-1, atlantic)
        
        for j in range(len(heights[0])):
            dfs(0, j, pacific)
            dfs(len(heights)-1, j, atlantic)
        
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        return res