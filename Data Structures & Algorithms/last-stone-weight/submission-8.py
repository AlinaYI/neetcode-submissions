class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # 这里拿的是最大的石头
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)

            if stone1 != stone2:
                diff = abs(stone1) - abs(stone2)
                heapq.heappush(maxHeap, -diff)
        return abs(maxHeap[0]) if maxHeap else 0
        