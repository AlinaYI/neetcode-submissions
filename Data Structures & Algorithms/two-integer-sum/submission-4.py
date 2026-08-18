class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # value:idx
        hashmap = {}
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], idx]
            hashmap[n] = idx
        return -1