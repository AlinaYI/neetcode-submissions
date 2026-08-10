class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # weighted
        # dijkstra
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
            for nextT, nei in graph[curr]:
                heapq.heappush(minHeap, (nextT+time, nei))
            
        return res if len(seen) == n else -1