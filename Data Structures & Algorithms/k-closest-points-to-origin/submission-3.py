class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        这里就是希望要klargest
        那就是maintain一个 k 的minHeap
        如果超过k了，就把大的pop出来
        '''

        maxHeap = []
        for point in points:
            x, y = point[0], point[1]
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(maxHeap, (-dist, x, y))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res= []
        for dist, x, y in maxHeap:
            res.append([x,y])
        return res