class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # kcloseest
        # 那就要从小到大
        # minHeap
        maxHeap = []
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(maxHeap, (-dist, point))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        for dist, point in maxHeap:
            res.append(point)
        return res
