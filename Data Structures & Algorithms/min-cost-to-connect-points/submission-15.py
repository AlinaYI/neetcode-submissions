class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # DSU
        # MST
        graph = defaultdict(list)
        for i in range(len(points)):
            x, y = points[i]
            for j in range(i+1, len(points)):
                x2,y2 = points[j]

                dist = abs(x2-x) + abs(y2-y)
                graph[i].append((dist, j))
                graph[j].append((dist, i))
        
        minHeap = [(0,0)] # cost, node
        seen = set()
        res = 0
        while minHeap:
            dist, curr = heapq.heappop(minHeap)

            if curr in seen:
                continue

            seen.add(curr)
            res += dist
            for neiCost,nei in graph[curr]:
                heapq.heappush(minHeap, (neiCost, nei))
        return res 
