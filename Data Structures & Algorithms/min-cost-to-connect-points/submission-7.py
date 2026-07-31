class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # MST
        graph = defaultdict(list)
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1, len(points)):
                x2,y2 = points[j]

                dist = abs(x1-x2) + abs(y1-y2)
                graph[i].append((dist, j))
                graph[j].append((dist,i))


        # dist, x,y
        minHeap = [(0,0)]
        seen = set()
        res = 0
        while minHeap:
            currDist, point = heapq.heappop(minHeap)

            if point not in seen:
                seen.add(point)
                res += currDist
                for dist, nei in graph[point]:
                    if nei not in seen:
                        heapq.heappush(minHeap, (dist, nei))
        return res if len(seen) == len(points) else 0

