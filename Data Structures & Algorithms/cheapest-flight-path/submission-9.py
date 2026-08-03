class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # dijkstra
        graph = defaultdict(list)
        for start, end, price in flights:
            graph[start].append((price, end))
        
        # price, curr, flight_time
        minHeap = [(0, src, 0)]
        seen = {}
        while minHeap:
            price, curr, flight_time = heapq.heappop(minHeap)

            if curr == dst and flight_time -1 <= k:
                return price
        
            if curr not in seen or seen[curr] > flight_time:
                seen[curr] = flight_time
                for neiPrice, nei in graph[curr]:
                    heapq.heappush(minHeap, (price+neiPrice, nei, flight_time+1))

        return -1