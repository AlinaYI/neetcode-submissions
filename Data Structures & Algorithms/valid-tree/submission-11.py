class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # 这里主要就是不能有环
        
        if len(edges) != n-1:
            return False
        
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q = deque([0])
        seen = {0}
        while q:
            curr = q.popleft()

            for nei in graph[curr]:
                if nei not in seen:
                    q.append(nei)
                    seen.add(nei)
        return len(seen) == n