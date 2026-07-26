class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self, node):
        curr = node
        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False
        
        if self.size[root_u] < self.size[root_v]:
            root_u , root_v = root_v, root_u
        
        self.parent[root_v] = root_u
        self.size[root_u] += self.size[root_v]
        return True

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        dsu = DSU(row*col)
        cell = []
        for i in range(row):
            for j in range(col):
                cell.append((grid[i][j], i, j))

        cell.sort()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        seen = set()
        for height, i, j in cell:
            seen.add((i,j))
            curr = col*i + j

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) in seen:
                    nei = col * ni + nj
                    dsu.union(curr, nei)
                
            if dsu.find(0) == dsu.find(row*col - 1):
                return height
