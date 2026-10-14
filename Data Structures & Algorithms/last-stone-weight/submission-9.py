class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        self.maxHeap = []
        for s in stones:
            heapq.heappush(self.maxHeap, -s)
        
        while len(self.maxHeap) > 1:
            stone1 = heapq.heappop(self.maxHeap)
            stone2 = heapq.heappop(self.maxHeap)

            value = abs(stone1) - abs(stone2)
            if value > 0:
                heapq.heappush(self.maxHeap, -value)
        
        return abs(self.maxHeap[0]) if self.maxHeap else 0