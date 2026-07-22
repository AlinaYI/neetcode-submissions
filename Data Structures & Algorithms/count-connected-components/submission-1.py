class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        seen = set()
        def dfs(node):
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        res = 0
        for node in range(n):
            if node not in seen:
                dfs(node)
                res += 1
        return res