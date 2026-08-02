class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        '''
        这里需要的是kcloest
        也就是需要算出每一个points距离(0,0)的距离，
        然后我们每次要pop出里的最远的，这样就能留下最近的
        输出的就是maxHeap[0]
        '''

        maxHeap = []
        for x, y in points:
            dist = math.sqrt((x-0)**2 + (y-0)**2)
            
            heapq.heappush(maxHeap, (-dist, [x,y]))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        while maxHeap:
            dist, point = heapq.heappop(maxHeap)
            res.append(point)
        return res