class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        while len(maxHeap) > 1:
            stone1 =  - heapq.heappop(maxHeap)
            stone2 = - heapq.heappop(maxHeap)

            if stone1 == stone2:
                continue
            else:
                newStone = abs(stone1-stone2)
                heapq.heappush(maxHeap, -newStone)
            
        return -maxHeap[-1] if len(maxHeap) == 1 else 0