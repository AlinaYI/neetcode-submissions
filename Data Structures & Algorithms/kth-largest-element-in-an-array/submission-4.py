class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 需要k lartger，也就是需要pop出来小的
        self.minHeap = []
        for n in nums:
            heapq.heappush(self.minHeap, n)
            if len(self.minHeap) > k:
                heapq.heappop(self.minHeap)
        return self.minHeap[0]