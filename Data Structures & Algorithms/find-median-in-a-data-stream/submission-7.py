class MedianFinder:

    def __init__(self):
        # [1,2,3]-> maxHeap, everyTime pop max
        # [4,5,6]-> minHeap, everyTime pop min
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        
        if self.maxHeap and num < -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        # check abs(length between heaps > 2?)
        if abs(len(self.minHeap)-len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap):
                n = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -n)
            else:
                n = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -n)

    def findMedian(self) -> float:

        if len(self.minHeap) == len(self.maxHeap):
            num1 = self.minHeap[0]
            num2 = self.maxHeap[0] *-1
            return (num1+num2)/2
        else:
            if len(self.minHeap) > len(self.maxHeap):
                return self.minHeap[0]
            else:
                return self.maxHeap[0]*-1
        
        