class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # 就是不能有循环
        # 这里就是可以用dfs/bfs来看是不是有循环

        if len(edges) != n - 1:
            return False
            
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q = deque([0])
        seen = {0}
        while q:
            curr = q.popleft()
            
            for nei in graph[curr]:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)
        return len(seen) == n