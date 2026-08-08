class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # want the max stone
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)

            if abs(stone1) == abs(stone2):
                continue
            else:
                rest = abs(stone1 - stone2)
                heapq.heappush(maxHeap, -rest)
        return -maxHeap[0] if maxHeap else 0