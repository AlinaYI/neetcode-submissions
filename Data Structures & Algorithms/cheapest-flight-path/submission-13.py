class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # weight, dijkstra
        graph = defaultdict(list)
        seen = {} # 需要记录状态，在里面就说明之前就到过，但是要更新minmum

        for start, end, spend in flights:
            graph[start].append( (spend, end) )

        # spend, curr, flightTime
        minHeap = [ (0, src, 0) ]
        while minHeap:
            spend, curr, flightTime = heapq.heappop(minHeap)

            if curr == dst and flightTime -1 <= k:
                return spend

            if curr not in seen or seen[curr] > flightTime:
                seen[curr] = flightTime

                for neiSpend, nei in graph[curr]:
                    heapq.heappush(minHeap, (neiSpend + spend, nei, flightTime+1) )

        return -1 