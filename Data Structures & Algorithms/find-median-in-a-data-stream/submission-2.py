'''
这道题就是每次要加入数字的时候，返回当前nums的中位数
如果是奇数长度，就是最中间的数字，
如果是偶数长度，就是最中间两个数字的平均值

如果每次加入都排序，然后取中间的话， 每次排序都是Onlogn

这里希望做到的是Ologn

可以用heap
maxHeaop    minHeap   
[2, 1]       [3, 4, 5]

这样就是odd，取多的那个 maxHeap 的max， minHeap的min
'''
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        
    def addNum(self, num: int) -> None:
        
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        # 2. 平衡两个 heap 的大小
        if len(self.maxHeap) > len(self.minHeap) + 1:
            value = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, value)

        elif len(self.minHeap) > len(self.maxHeap) + 1:
            value = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -value)

    def findMedian(self) -> float:
        
        if len(self.minHeap) == len(self.maxHeap):
            numMaxHeap = self.maxHeap[0] * -1
            numMinHeap = self.minHeap[0]
            return (numMaxHeap + numMinHeap)/2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        
        elif len(self.minHeap) < len(self.maxHeap):
            return self.maxHeap[0] * -1