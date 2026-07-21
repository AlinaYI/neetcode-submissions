class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        visited = set()
        res = 0

        def bfs(start):
            q = deque([start])
            visited.add(start)

            while q:
                node = q.popleft()

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
                        
        for node in range(n):
            if node not in visited:
                res += 1
                bfs(node)
        return res
