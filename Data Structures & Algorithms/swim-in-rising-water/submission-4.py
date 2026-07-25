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
            root_u, root_v = root_v, root_u
        
        self.parent[root_v] = root_u
        self.size[root_u] += self.size[root_v]

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        cell = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cell.append((grid[i][j], i, j))
        
        cell.sort()

        dsu = DSU(len(grid)*len(grid))
        seen = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        for height, i, j in cell:
            seen.add((i,j))
            curr = i * len(grid) + j

            for di, dj in directions:
                ni, nj = di + i, dj + j

                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni,nj) in seen:
                    nei = ni * len(grid) + nj
                    dsu.union(curr, nei)
            
            if dsu.find(0) == dsu.find(len(grid)*len(grid) - 1):
                return height