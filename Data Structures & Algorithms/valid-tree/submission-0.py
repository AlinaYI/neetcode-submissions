class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)
        
        seen = set()
        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)
            for neighbour in adj_list[node]:
                dfs(neighbour)
        dfs(0)
        return len(seen) == n