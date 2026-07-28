class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxheap =[]

        count = Counter(nums)

        for val, fre in count.items():
            heapq.heappush(maxheap, (-fre, val))
        
        for i in range(k):
            res.append(heapq.heappop(maxheap)[1])

        return res