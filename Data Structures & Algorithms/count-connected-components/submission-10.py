class DSU:
    def __init__(self):
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
        
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node):
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        res = 0
        seen = set()
        for node in range(n):
            if node not in seen:
                seen.add(node)
                dfs(node)
                res += 1
        return res
        