class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        # 永远maintain一个 windowSize为k的 heap queue
        # 然后每次 pop出来最小的，这样heap里面能pop出来的就是klargest
        self.minHeap = []
        self.k = k
        for n in nums:
            heapq.heappush(self.minHeap, n)
            if len(self.minHeap) > k:
                heapq.heappop(self.minHeap) 
            
    def add(self, val: int) -> int:

        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
