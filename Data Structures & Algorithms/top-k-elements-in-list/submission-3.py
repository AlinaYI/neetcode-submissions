class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        max_heap = []
        for key, freq in count.items():
            heapq.heappush(max_heap, (-freq, key))
        
        res = []
        for i in range(k):
            fre, key = heapq.heappop(max_heap)
            res.append( key )
        return res
