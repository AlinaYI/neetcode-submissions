class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # weighted map
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append((target, time))
        
        # time, k(start point)
        min_heap = [(0, k)]
        visited = set()
        res = 0

        while min_heap:
            time, curr = heapq.heappop(min_heap)

            if curr in visited:
                continue
            
            visited.add(curr)
            res = time

            for neighbor, weight in graph[curr]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (time + weight, neighbor))
            
        if len(visited) == n:
            return res
        
        return -1
