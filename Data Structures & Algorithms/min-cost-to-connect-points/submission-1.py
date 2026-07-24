class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]

                distance = abs(x1-x2) + abs(y1 - y2)
                graph[i].append([distance, j])
                graph[j].append([distance, i])
        
        res = 0
        seen = set()
        min_heap = [(0,0)]
        while len(seen) < len(points):
            cost, i = heapq.heappop(min_heap)

            if i in seen:
                continue
            
            seen.add(i)
            res += cost
            for neiCost, nei in graph[i]:
                if nei not in seen:
                    heapq.heappush(min_heap, [neiCost, nei])
        return res