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

        if rootU == rootV:
            return False
        
        if self.size[rootU] < self.size[rootV]:
            rootU, rootV = rootV, rootU
        
        self.size[rootU] += self.size[rootV]
        self.parent[rootV] = self.parent[rootU]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        dsu = DSU(len(edges)+1)
        for u, v in edges:
            if not dsu.union(u, v):
                return [u,v]
        return []