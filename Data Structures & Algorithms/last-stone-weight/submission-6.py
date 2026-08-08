class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # 要拿最大的
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            stone1 = abs(heapq.heappop(maxHeap))
            stone2 = abs(heapq.heappop(maxHeap))

            if stone1 != stone2:
                heapq.heappush(maxHeap, -abs(stone1 - stone2))
        return abs(maxHeap[0]) if maxHeap else 0
            