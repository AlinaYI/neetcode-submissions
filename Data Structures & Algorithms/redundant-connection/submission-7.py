class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph =  defaultdict(list)
        def dfs(u, v, seen):
            if u == v:
                return True
            seen.add(u)
            for nei in graph[u]:
                if nei not in seen:
                    if dfs(nei, v, seen):
                        return True
            return False
        
        for u,v in edges:
            if dfs(u,v, set()):
                return [u,v]
            graph[u].append(v)
            graph[v].append(u)