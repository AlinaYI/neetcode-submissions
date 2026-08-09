class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # 要移除最大的
        maxHeap= []
        for x, y in points:
            dist = math.sqrt(x**2+y**2)
            heapq.heappush(maxHeap, (-dist, x, y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

            
        
        res = []
        for dist, x, y in maxHeap:
            res.append( [x,y] )
        return res