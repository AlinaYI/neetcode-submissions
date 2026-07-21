class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_nums = Counter(nums)
        heap =[]
        res = []

        for key, val in count_nums.items():
            heapq.heappush(heap, [-val, key])
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res