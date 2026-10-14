class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # 这里要pop出来大的，所以是maxHeap
        self.maxHeap = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(self.maxHeap, (-dist, point) )

            if len(self.maxHeap) > k:
                heapq.heappop(self.maxHeap)
        
        res = []
        for _, point in self.maxHeap:
            res.append(point)
        return res
