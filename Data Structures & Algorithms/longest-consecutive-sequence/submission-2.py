class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        nums_set = set(nums)
        res = 0

        for n in nums:
            if n-1 not in nums_set:
                length = 1
                while n + length in nums_set:
                    length += 1
                res = max(res, length)
        return res