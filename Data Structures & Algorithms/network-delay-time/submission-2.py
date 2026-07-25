class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        weighted map
        dijkstra
        '''

        graph = defaultdict(list)
        for start, end, cost in times:
            graph[start].append( (end, cost) )
        
        # total_cost, start
        min_heap = [ (0, k) ]
        seen = set()
        res = 0
        while min_heap:
            curr_cost, curr = heapq.heappop(min_heap)
            
            if curr not in seen:
                res = curr_cost
                seen.add(curr)
                for nei, cost in graph[curr]:
                    if nei not in seen:
                        heapq.heappush(min_heap, (cost + curr_cost, nei) ) 

        return res if len(seen) == n else -1