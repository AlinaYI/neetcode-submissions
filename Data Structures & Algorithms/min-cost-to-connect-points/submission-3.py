class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                graph[i].append( (dist, j) )
                graph[j].append( (dist, i) )
        
        min_heap = [ (0, 0) ]
        seen = set()
        res = 0

        while min_heap:
            cost, node = heapq.heappop(min_heap)

            if node not in seen:
                seen.add(node)
                res += cost
                for dist, nei in graph[node]:
                    if nei not in seen:
                        heapq.heappush(min_heap, (dist, nei))
        
        return res if len(seen) == len(points) else 0