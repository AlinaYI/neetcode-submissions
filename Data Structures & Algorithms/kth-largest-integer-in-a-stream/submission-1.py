# 想要klargest
# 那我们就maintain一个从小到大的window -> window size 是k
# 超过这个size k，就把小的pop出来

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k

        for n in nums:
            heapq.heappush(self.minHeap, n)

            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)
        return self.minHeap[0]
