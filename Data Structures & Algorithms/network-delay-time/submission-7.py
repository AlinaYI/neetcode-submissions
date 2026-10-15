class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # dijkstra, weighted map
        graph = defaultdict(list)
        for start, end, time in times:
            graph[start].append( (time, end) )

        minHeap = [(0, k)]
        seen = set()
        res = 0
        while minHeap:
            time, curr = heapq.heappop(minHeap)

            if curr in seen:
                continue
            
            seen.add(curr)
            res = time
            for neiT, neiE in graph[curr]:
                if neiE not in seen:
                    heapq.heappush(minHeap, (time+neiT, neiE))
        return res if len(seen) == n else -1