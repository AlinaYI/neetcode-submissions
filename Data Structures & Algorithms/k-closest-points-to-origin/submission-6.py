class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 要最cloest
        # 就是把大的pop出去
        # maxHeap
        maxHeap = []
        for i in range(len(points)):
            x, y = points[i]
            dist = abs(x**2+y**2)
            heapq.heappush(maxHeap, (-dist, x, y))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        for dist, x, y in maxHeap:
            res.append( [x,y] )
        return res