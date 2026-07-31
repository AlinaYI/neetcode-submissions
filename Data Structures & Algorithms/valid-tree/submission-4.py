class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        看有没有环，没有环就是valid node
        dfs/bfs
        '''
        if len(edges) != n-1:
            return False
            
        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)
            for nei in graph[node]:
                dfs(nei)

        seen = set() 
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        dfs(0)
        return len(seen) == n
