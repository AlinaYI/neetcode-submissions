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
        rootU = self.find(u)
        rootV = self.find(v)

        if rootV == rootU:
            return False
        
        if self.size[rootU] < self.size[rootV]:
            rootU, rootV = rootV, rootU
        
        self.parent[rootV]=rootU
        self.size[rootU] += self.size[rootV]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # DSU
        # MST
        edges = []
        for i in range(len(points)):
            x, y = points[i]
            for j in range(i+1, len(points)):
                x2,y2 = points[j]

                dist = abs(x2-x) + abs(y2-y)
                edges.append((dist, j, i))
        
        edges.sort()
        res = 0
        dsu = DSU(len(points))
        for dist, i, j in edges:
            if dsu.union(i,j):
                res += dist
        return res