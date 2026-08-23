class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # dijkstra, wighted
        # seen: {end: price}
        # minHeap = [curr, price, flight_Time]
        # TC: O(ke log(kv))
        # sc: O(kV + E)

        # for loop, < flightTime
        # prices = [] -> idx, 代表城市
        # initial start, each time update minPrice
        # return prices[dst]? -> yes, return price, no, return -1
        # TC: 外层跑 k+1次， 然后每次扫所有的edge
        #      O(KE)
        # SC: O(V)

        prices = [float("inf")]*n
        prices[src] = 0

        for _ in range(k+1):
            temp = prices.copy()
            for start, end, price in flights:
                if prices[start] != float("inf"):
                    temp[end] = min(temp[end], prices[start]+ price)
            prices = temp
        return prices[dst] if prices[dst] != float("inf") else -1