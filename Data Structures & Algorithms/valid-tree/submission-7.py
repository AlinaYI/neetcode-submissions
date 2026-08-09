class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        # 看是不是valid，就有没有loop
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        q = deque([0])
        seen = {0}
        while q:
            curr = q.popleft()

            for nei in graph[curr]:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)
        return len(seen) == n