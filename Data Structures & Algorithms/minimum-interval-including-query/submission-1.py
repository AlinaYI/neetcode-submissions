class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        res = {}
        idx = 0

        for q in sorted(queries):
            while idx < len(intervals) and intervals[idx][0] <= q:
                left, right = intervals[idx]
                heapq.heappush(minHeap, (right-left+1, right))
                idx += 1
            
            # pop 掉不需要的
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            res[q] = minHeap[0][0] if minHeap else -1
        
        return [res[q] for q in queries]