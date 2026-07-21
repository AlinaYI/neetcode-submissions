class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)

        return len(nums_set) != len(nums)