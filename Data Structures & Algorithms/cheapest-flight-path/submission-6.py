class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, price in flights:
            graph[start].append((price, end))
        
        # total_cost, satrt, flight_time
        min_heap = [(0, src, 0)]
        seen = {} # maybe double visited, in seen, visited, flight_time compare

        while min_heap:
            curr_cost, curr_city, flight_time = heapq.heappop(min_heap)

            if curr_city == dst and flight_time - 1 <= k:
                return curr_cost
           
            if curr_city not in seen or seen[curr_city] > flight_time:
                seen[curr_city] = flight_time
                for price, nei in graph[curr_city]:
                    heapq.heappush(min_heap, (price+curr_cost, nei, flight_time + 1))
        
        return -1