class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        countN = Counter(nums)
        return heapq.nlargest(k, countN.keys(), key=countN.get)