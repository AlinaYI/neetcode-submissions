class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for i in range(len(points)):
            # first point:
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                graph[i].append((dist, j))
                graph[j].append((dist, i))
        
        minHeap = [[0, 0]]
        res = 0
        seen = set()
        while minHeap:
            dist, curr = heapq.heappop(minHeap)
            if curr in seen:
                continue
            seen.add(curr)
            res += dist
            for d, nei in graph[curr]:
                if nei not in seen:
                    heapq.heappush(minHeap, (d, nei))
        return res 
            