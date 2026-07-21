class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # maxi heap
        heap = []
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap,(-distance, point[0], point[1]) )
                    
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for _ in range(len(heap)):
            distance, point1, point2 = heapq.heappop(heap)
            res.append([point1, point2])
        return res