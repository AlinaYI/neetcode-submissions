class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        duplicated = set()
        hashmap = {}
        res = set()
        # first = nums[i]
        for i in range(len(nums)):
            if nums[i] in duplicated:
                continue
            duplicated.add(nums[i])
            target = 0 - nums[i]

            # second: nums[j]
            for j in range(i+1, len(nums)):
                diff = target - nums[j]
                if diff in hashmap and hashmap[diff] == i:
                    res.add( tuple(sorted( (nums[i], nums[j], diff) )) )
                hashmap[nums[j]] = i
        return list(res)
