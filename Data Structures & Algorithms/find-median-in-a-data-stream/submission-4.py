class MedianFinder:

    def __init__(self):
        # [1,2,3,4,5,6]
        # 存一个maxHeap， minHeap
        # maxHeap存前半部分，minHeap存后半部分
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
         
        if abs(len(self.maxHeap) - len(self.minHeap)) > 1:
            if len(self.maxHeap) > len(self.minHeap):
                num = heapq.heappop(self.maxHeap) *-1
                heapq.heappush(self.minHeap, num)
            else:
                num = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -num)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            Num1 = self.maxHeap[0] * -1
            Num2 = self.minHeap[0]

            return (Num1 + Num2)/2
        else:
            if len(self.minHeap) > len(self.maxHeap):
                return self.minHeap[0]
            else:
                return self.maxHeap[0]*-1
            
        