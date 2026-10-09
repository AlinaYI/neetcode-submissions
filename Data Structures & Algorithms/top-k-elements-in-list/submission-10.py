class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # if k == len(nums):
        #     return nums

        # countN = Counter(nums)
        # return heapq.nlargest(k, countN.keys(), key=countN.get)

################################
        maxHeap = []
        countN = Counter(nums)
        for key, freq in countN.items():
            heapq.heappush(maxHeap, (-freq, key))
        
        res = []
        for _ in range(k):
            res.append( heapq.heappop(maxHeap)[1] )
        return res

