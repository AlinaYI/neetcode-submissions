class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        看有没有环，没有环就是valid node
        dfs/bfs
        '''
        if len(edges) != n-1:
            return False
        
        seen = {0}
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)   
        
        q = deque([0])
        while q:
            curr = q.popleft()

            for nei in graph[curr]:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)
        return len(seen) == n