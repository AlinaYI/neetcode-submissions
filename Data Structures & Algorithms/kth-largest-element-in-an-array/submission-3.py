class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maxHeap
        maxHeap = []
        for n in nums:
            heapq.heappush(maxHeap, n)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return maxHeap[0]