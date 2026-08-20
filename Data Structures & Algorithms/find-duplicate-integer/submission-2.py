class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = set()
        for n in nums:
            if n in dup:
                return n
            dup.add(n)
        return -1