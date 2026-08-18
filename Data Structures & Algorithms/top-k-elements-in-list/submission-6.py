class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxFreq = []
        count = Counter(nums)

        for n, freq in count.items():
            heapq.heappush(maxFreq, (-freq, n))
        
        res = []
        for _ in range(k):
            _, n = heapq.heappop(maxFreq)
            res.append(n)
        return res