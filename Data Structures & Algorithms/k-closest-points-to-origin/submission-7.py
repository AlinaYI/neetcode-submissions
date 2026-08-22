class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # 需要第k个最靠近的，那就把距离远的pop
        # maintain windowSize == k
        maxHeap = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(maxHeap, (-dist, x, y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        for dist, x, y in maxHeap:
            res.append([x, y])
        return res