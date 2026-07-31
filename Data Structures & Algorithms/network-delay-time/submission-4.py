class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra
        graph = defaultdict(list)
        for start, end, price in times:
            graph[start].append((price, end))
        
        minHeap = [(0, k)]
        seen = set()
        while minHeap:
            time, curr = heapq.heappop(minHeap)

            if curr in seen:
                continue

            res = time
            seen.add(curr)
            for price, nei in graph[curr]:
                heapq.heappush(minHeap, (price+time, nei))
        return res if len(seen) == n else -1
