class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append((target, time))
        
        min_heap = [(0, k)]
        seen = set()
        res = 0
        while min_heap:
            time, curr = heapq.heappop(min_heap)

            if curr not in seen:
                seen.add(curr)
                res = time

                for nei, weight in graph[curr]:
                    heapq.heappush(min_heap, (time + weight, nei))
        
        
        return res if len(seen) == n else -1
