class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)

        for start, target, ticket in flights:
            graph[start].append((target, ticket))
        
        # ticket, target, stop
        min_heap = [(0, src, 0)]
        seen = {}
        while min_heap:

            cost, curr_location, flights_used  = heapq.heappop(min_heap)

            if curr_location == dst and flights_used  - 1 <= k:
                return cost

            if curr_location not in seen or seen[curr_location] > flights_used :
                seen[curr_location] = flights_used 
                for nei, price in graph[curr_location]:
                    heapq.heappush(min_heap, (cost + price, nei, flights_used  + 1))
        return -1
            