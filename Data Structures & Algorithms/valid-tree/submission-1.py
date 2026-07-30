class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        valid tree 不是loop
        '''
        if len(edges) != n-1:
            return False
            
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        q = deque([0])
        seen = {0}
        while q:
            curr = q.popleft()
            
            for nei in graph[curr]:
                if nei not in seen:
                    q.append(nei)
                    seen.add(nei)
        
        return len(seen) == n