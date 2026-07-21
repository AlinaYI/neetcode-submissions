class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        heap = []
        count_nums = Counter(nums)
        for key,val in count_nums.items():
            heapq.heappush(heap, [-val,key])
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res