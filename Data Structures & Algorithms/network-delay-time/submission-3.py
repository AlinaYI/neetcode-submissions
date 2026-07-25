class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        weighted dijkstra
        '''

        graph = defaultdict(list)
        for start, end, time in times:
            graph[start].append((time, end))
        
        min_heap = [(0, k)]
        res = 0
        seen = set()
        while min_heap:
            curr_time, start = heapq.heappop(min_heap)

            if start in seen:
                continue

            res = curr_time
            seen.add(start)
            for time, nei in graph[start]:
                if nei not in seen:
                    heapq.heappush(min_heap, (time + curr_time, nei))

        return res if len(seen) == n else -1


