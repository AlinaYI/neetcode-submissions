class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        duplicated = set()
        res = set()
        hashmap = {}

        # first number
        for i in range(len(nums)):
            if nums[i] in duplicated:
                continue
            diff = 0-nums[i]

            # second: nums[j]
            for j in range(i+1, len(nums)):
                third = diff - nums[j]
                if third in hashmap and hashmap[third] == i:
                    res.add( tuple(sorted( (nums[i], nums[j], third) )) )
                hashmap[nums[j]] = i
        
        return list(res)