class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # weighted map
        # dijkstra
        graph = defaultdict(list)
        for start, end, time in times:
            graph[start].append((time, end))
        
        minHeap = [(0, k)]
        seen = set()
        res = 0
        while minHeap:
            time, curr = heapq.heappop(minHeap)
            
            if curr in seen:
                continue
            seen.add(curr)
            res = time
            for t, nei in graph[curr]:
                if nei not in seen:
                    heapq.heappush(minHeap, (t+time, nei))
        return res if len(seen) == n else -1
