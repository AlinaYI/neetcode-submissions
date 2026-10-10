class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        duplicate = set()
        res = set()
        hashmap = {}

        # first number
        for i in range(len(nums)):

            if nums[i] in duplicate:
                continue
            duplicate.add(nums[i])
            target = - nums[i]

            # second
            for j in range(i+1, len(nums)):
                third = target - nums[j]
                if third in hashmap and hashmap[third] == i:
                    res.add( tuple(sorted((nums[i], nums[j], third) )) )
                hashmap[nums[j]] = i
        return [list(x) for x in res]