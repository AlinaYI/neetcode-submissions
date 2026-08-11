class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        def dfs(node, target, seen):
            if node == target:
                return True
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    if dfs(nei, target, seen):
                        return True
            return False

        for a,b in edges:
            if dfs(a, b, set()):
                return [a,b]
            graph[a].append(b)
            graph[b].append(a)