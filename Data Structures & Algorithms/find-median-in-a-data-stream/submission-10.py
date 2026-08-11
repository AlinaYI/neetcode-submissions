class MedianFinder:

    def __init__(self):
        
        # [1,2,3,4,5,6]
        # 前半部分maintain maxHeap，永远pop出来最大的
        # 后半部分maintain minHeap，永远pop出来最小的
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        
        # 先加
        # 如果两个Heap的差值 > 1, pop len长的给len小的
        if not self.maxHeap or num < self.maxHeap[0] *-1:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        if abs(len(self.minHeap)-len(self.maxHeap)) > 1:
            if len(self.maxHeap) > len(self.minHeap):
                num = heapq.heappop(self.maxHeap) * -1
                heapq.heappush(self.minHeap, num)
            else:
                num = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -num)

    def findMedian(self) -> float:

        # 1. equal length -> return (n from minHeap + n from maxHeap)/2
        if len(self.minHeap) == len(self.maxHeap):
            num1 = self.maxHeap[0] *-1
            num2 = self.minHeap[0]
            return (num1+num2)/2
        # 2. nonequal length -> return (n from lager length)
        else:
            if len(self.maxHeap) > len(self.minHeap):
                num = self.maxHeap[0] *-1
                return num
            else:
                num = self.minHeap[0]
                return num