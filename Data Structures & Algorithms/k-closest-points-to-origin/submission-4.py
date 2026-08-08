class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        maxHeap = []
        for x, y in points:
            dist = math.sqrt(x**2+y**2)
            heapq.heappush(maxHeap, (-dist, x,y))
        
        res = []
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        
        for dist, x, y in maxHeap:
            res.append([x,y])
        return res