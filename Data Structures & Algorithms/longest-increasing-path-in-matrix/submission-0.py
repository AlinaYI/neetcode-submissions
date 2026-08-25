from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        这道题就是要找longest incresing path
        就是有四个方向
        '''
        # top down
        @cache
        def dfs(i,j):
            res = 1
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<row and 0<=nj<col and matrix[ni][nj] > matrix[i][j]:
                    res = max(res, 1+dfs(ni, nj))
            return res
        
        row = len(matrix)
        col = len(matrix[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        ans = 0
        for i in range(row):
            for j in range(col):
                ans = max(ans, dfs(i,j))
        return ans
