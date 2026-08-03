class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # MST
        graph = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                graph[i].append((dist, j))
                graph[j].append((dist, i))
        
        # dist, point
        minHeap = [(0,0)]
        res = 0
        seen = set()
        while minHeap:
            currDist, point = heapq.heappop(minHeap)
            if point in seen:
                continue

            seen.add(point)
            res += currDist
            for neiDist, nei in graph[point]:
                heapq.heappush(minHeap, (neiDist, nei))
        
        return res