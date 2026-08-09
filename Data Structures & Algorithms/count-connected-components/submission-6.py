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
        
        if self.size[rootU] > self.size[rootV]:
            rootU, rootV = rootV, rootU
        
        self.parent[rootV] = rootU
        self.size[rootU] += self.size[rootV]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res