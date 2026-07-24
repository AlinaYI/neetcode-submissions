class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]* (n)
    
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
        
        if self.size[root_u] > self.size[root_v]:
            root_u, root_v = root_v, root_u
        
        self.parent[root_u] = root_v
        self.size[root_v] += self.size[root_u]

        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dsu = DSU(len(points))
        edges = []
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]

                dist = abs(x1-x2) + abs(y1-y2)
                edges.append((dist, i, j))
        
        edges.sort()
        res = 0
        for dist, u, v in edges:
            if dsu.union(u, v):
                res += dist
        return res