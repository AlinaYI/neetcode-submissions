class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(points)):
            x, y = points[i]
            for j in range(i+1, len(points)):
                x2,y2 = points[j]

                dist = abs(x2-x) + abs(y2-y)
                graph[i].append((dist, j))
                graph[j].append((dist, i))

        # cost,node
        minHeap = [(0,0)]
        seen = set()
        res = 0
        while minHeap:
            cost, node = heapq.heappop(minHeap)

            if node in seen:
                continue
            seen.add(node)
            res += cost

            for neiCost, nei in graph[node]:
                heapq.heappush(minHeap, (neiCost, nei))
        return res