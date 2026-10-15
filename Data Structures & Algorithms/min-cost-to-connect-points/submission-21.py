class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # {point1: (dist, point2)}
        graph = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]

                dist = abs(x1-x2) + abs(y1-y2)
                graph[i].append( (dist, j) )
                graph[j].append( (dist, i) )

        # cost, node
        minHeap = [ (0,0) ]
        seen = set()
        res = 0
        while minHeap:
            cost, curr = heapq.heappop(minHeap)

            if curr in seen:
                continue
            seen.add(curr)
            res += cost

            for neiC, neiN in graph[curr]:
                heapq.heappush(minHeap, (neiC, neiN))
        return res