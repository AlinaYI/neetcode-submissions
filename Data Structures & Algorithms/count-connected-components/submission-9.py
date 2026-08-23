class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)
            graph[u].append(v)

        def dfs(i):
            seen.add(i)
            for nei in graph[i]:
                if nei not in seen:
                    dfs(nei)

        seen = set()
        res = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                res += 1
        return res