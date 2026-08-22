class MedianFinder:

    def __init__(self):
        
        # [1,2,3,4,5,6]
        # 想要中间的，那就是可以用heap
        # 前半段要maxHeap --> 给小部分的最大的
        # 后半段要minHeap --> 给大部分的最小的
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        # rebalance
        if len(self.maxHeap) > len(self.minHeap) + 1:
            num = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, num)

        elif len(self.minHeap) > len(self.maxHeap) + 1:
            num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -num)

    def findMedian(self) -> float:
        
        if len(self.minHeap) == len(self.maxHeap):
            n1 = self.minHeap[0]
            n2 = self.maxHeap[0]*(-1)

            return (n1+n2)/2
        elif len(self.minHeap) > len(self.maxHeap):
            n = self.minHeap[0]
            return n
        else:
            n = self.maxHeap[0]*(-1)
            return n
        