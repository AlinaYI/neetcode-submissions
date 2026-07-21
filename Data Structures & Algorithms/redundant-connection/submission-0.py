class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)

        def dfs(curr, target, seen):
            if curr == target:
                return True
            
            seen.add(curr)

            for neighbor in graph[curr]:
                if neighbor not in seen:
                    if dfs(neighbor, target, seen):
                        return True
            
            return False
        
        for a,b in edges:
            if dfs(a, b, set()):
                return [a,b]
            
            graph[a].append(b)
            graph[b].append(a)