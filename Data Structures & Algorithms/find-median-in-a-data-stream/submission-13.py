class MedianFinder:

    def __init__(self):

        # [1, 2, 3, 4, 5, 6 ]
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        
        # add into maxHeap if maxheap is empty
        if not self.maxHeap or num < -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        if len(self.maxHeap) > len(self.minHeap) +1:
            num = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, num)
        elif len(self.minHeap) > len(self.maxHeap)+1:
            num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -num)

    def findMedian(self) -> float:
        
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            num1 = self.minHeap[0]
            num2 = -self.maxHeap[0]
            return (num1+num2)/2
        