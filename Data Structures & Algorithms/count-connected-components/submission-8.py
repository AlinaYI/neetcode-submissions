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