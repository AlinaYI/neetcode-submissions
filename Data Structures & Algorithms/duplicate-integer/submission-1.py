class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_lence = len(set(nums))
        return set_lence != len(nums)