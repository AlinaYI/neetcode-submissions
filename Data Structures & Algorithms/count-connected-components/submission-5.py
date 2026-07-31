class DSU:
    def __init__(self,n):
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

        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u,v in edges:
            if dsu.union(u,v):
                res -= 1
        return res