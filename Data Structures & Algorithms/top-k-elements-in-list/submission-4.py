class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        max_heap = []

        for key, fre in count.items():
            heapq.heappush(max_heap, (-fre, key))
        res = []
        for i in range(k):
            freq, key = heapq.heappop(max_heap)
            res.append(key)
        return res